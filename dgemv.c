/**
 * @copyright (c) 2020- King Abdullah University of Science and
 *                      Technology (KAUST). All rights reserved.
 **/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/time.h>
#include <math.h>
#include <assert.h>
#include <unistd.h>
#include <memory.h>
#ifdef USE_INTEL
#include <mkl.h>
#endif 

#ifdef USE_NVIDIA
#include <cuda.h>
#include <cuda_runtime.h>
#include <cuda_runtime_api.h>
#include <cublas_v2.h>
#endif

#ifdef USE_AMD

#endif

#ifdef USE_DOUBLE
#define real_t double
#else
#define real_t float
#endif 

int min(int a, int b){
  if(a < b) return a;
  return b;
}

int cmpfunc (const void * a, const void * b) {
   return ( *(double*)a - *(double*)b );
}

void csort(double *y, int arrlen){
  qsort(y, arrlen, sizeof(double), cmpfunc);
}

void saveresults(int m, int n, 
double tmax, double tmin, double t50, double t25, double t75,
double Pmean, double Bmean, char *type, char *filename){
  char record[100];
#ifdef USE_DOUBLE
  sprintf(record, "%d %d double %.3e %.3e %.3e %.3e %.3e %.3e %.3e %s\n", 
  m, n, tmax, tmin, t50, t25, t75, Pmean, Bmean, type);
#else
  sprintf(record, "%d %d single %.3e %.3e %.3e %.3e %.3e %.3e %.3e %s\n", 
  m, n, tmax, tmin, t50, t25, t75, Pmean, Bmean, type);
#endif 
  FILE *pf;
  if( access(filename, F_OK) == -1){
    pf = fopen(filename, "w");
    char str[] = "m   n   precision TimeMax(s) TimeMin(s) Time50th(s) Time25th(s) Time75Th(s) RelErr Bandwith(GB/s) ExpType\n";
    fwrite(str,1,sizeof(str),pf);
    fprintf(pf, "%s", record);
  }else{
    pf = fopen(filename, "a");
    fprintf(pf, "%s", record);
  }
  
  fclose(pf);
}

double gettime(void)
{
	struct timeval tp;
	gettimeofday( &tp, NULL );
	return tp.tv_sec + 1e-6 * tp.tv_usec;
}

void naive_impl(real_t *A, real_t* x, real_t *y, int m, int n){
  #pragma omp parallel for
  for(int i=0; i<m; i++){
    y[i] = (real_t)0.0;
    for(int j=0; j<n; j++){
      y[i] += A[i + j * m] * x[j];
    }
  }
}

void Initdata_cpu(real_t *A, real_t* x, real_t *y, int m, int n){
  memset(y, 0, sizeof(real_t) * n);
  for(int i=0; i<n; i++){
    x[i] = (real_t)rand() / (real_t)RAND_MAX;
  }
  for(int i=0; i<m; i++){
    for(int j=0; j<n; j++){
      A[i * n + j] = (real_t)rand() / (real_t)RAND_MAX;
    }
  }
}

double mean(double *y, int dim){
  double ret = 0.0;
  #pragma omp parallel for
  for(int i=0; i<dim; i++){
    ret += y[i];
  }
  ret /= dim;
  return ret;
}

double var(double *y, int dim){
  double mval = mean(y, dim);
  double s = 0.0;
  #pragma omp parallel for
  for(int i=0; i<dim; i++){
    s += (mval - y[i]) * (mval - y[i]);
  }
  s /= (dim - 1);
  return s;
}

double getquatile(double *y, double percent, int dim){
  return y[(int)(dim*percent)];
}

double checkcorrectness(real_t *y, real_t *ynaive, int dim, int sumdim){
  double *rerr = (double*)malloc(sizeof(double)*dim);
  for(int i=0; i<dim; i++){
    rerr[i] =fabs(y[i] - ynaive[i]) / fabs(ynaive[i]);
  }
  double meanval = mean(rerr, dim);
  free(rerr);
  return meanval;
}

#ifdef USE_NVIDIA
void checkcudaerror(cudaError_t st){
  if(st != cudaSuccess){
    printf("cuda status failed. \n");
    exit(0);
  }
}
void checkcudastatus(cublasStatus_t st){
  if(st != CUBLAS_STATUS_SUCCESS){
    printf("cuda status failed. \n");
    exit(0);
  }
}
#endif 

int main(int argc, const char* argv[])
{
  /**
   * @brief read input and init pointers
   * 
   */

  real_t *A, *y, *ynaive, *x;
  int m, n, nruns;
  int warmup = 10;
  real_t alpha, beta;
  char exptype[20];
  char filepath[100];
  printf ("\n This benchmark computes real vector y=alpha*A*x+beta*y, "
  "where A is matrix, y and x are vectors alpha and beta are scalars\n\n");
  alpha = 1.0;
  beta = 0.0;
  if(strcmp(argv[1], "fixed") == 0){
    assert(argc == 7);
    m = atoi(argv[2]);
    n = atoi(argv[3]);
    nruns = atoi(argv[4]);
    strcpy(exptype, argv[5]);
    strcpy(filepath, argv[6]);
  }else if(strcmp(argv[1], "range") == 0){
    assert(argc == 6);
  }else{
    printf("not recognized input size mode, exit. \n\n");
    exit(0);
  }

  printf(" 1) m : %d n: %d alpha: %f beta: %f nruns: %d\n\n", m, n, alpha, beta, nruns);



/**
 * @brief 
 * allocate memory
 */

#ifdef USE_INTEL
  A = (real_t *)mkl_malloc( m*n*sizeof( real_t ), 64 );
  x = (real_t *)mkl_malloc( n*sizeof( real_t ), 64 );
  y = (real_t *)mkl_malloc( m*sizeof( real_t ), 64 );
  ynaive = (real_t *)mkl_malloc( m*sizeof( real_t ), 64 );
  if (A == NULL || x == NULL || y == NULL) {
    printf( "\n ERROR: Can't allocate memory for matrices. Aborting... \n\n");
    mkl_free(A);
    mkl_free(x);
    mkl_free(y);
    return 1;
  }
  int threads = mkl_get_max_threads();
  char machinename[150];
  memset(machinename, 0, 150);
  gethostname(machinename,150);
  #ifdef USE_DOUBLE
  printf(" 2) use intel, mkl use %d threads and double precision on %s.\n\n", threads, machinename);
  #else
  printf(" 2) use intel, mkl use %d threads and single precision on %s.\n\n", threads, machinename);
  #endif 
#endif 

#ifdef USE_NVIDIA 
  cudaSetDevice(0); 
  // malloc host 
  A = (real_t *)malloc( m*n*sizeof( real_t ));
  x = (real_t *)malloc( n*sizeof( real_t ));
  y = (real_t *)malloc( m*sizeof( real_t ));
  ynaive = (real_t *)malloc( m*sizeof( real_t ));
  cudaError_t cudaStat;
  cublasStatus_t stat;
  cublasHandle_t handle;
	cudaEvent_t start, stop;
	cudaEventCreate(&start);
	cudaEventCreate(&stop);
  real_t *d_A, *d_y, *d_x;
  // malloc device
  cudaStat = cudaMalloc ((void**)&d_A, m*n*sizeof(real_t));
  checkcudaerror(cudaStat);
  cudaStat = cudaMalloc ((void**)&d_x, n*sizeof(real_t));
  checkcudaerror(cudaStat);
  cudaStat = cudaMalloc ((void**)&d_y, m*sizeof(real_t));
  checkcudaerror(cudaStat);
  stat = cublasCreate(&handle);
  checkcudastatus(stat);
  char machinename[150];
  memset(machinename, 0, 150);
  gethostname(machinename,150);
  #ifdef USE_DOUBLE
  printf(" 2) use nvidia %s and double precision on %s.\n\n", exptype, machinename);
  #else
  printf(" 2) use nvidia %s and single precision on %s.\n\n", exptype, machinename);
  #endif 
#endif 


/**
 * @brief init naive implementation and stat info.
 * 
 */
  printf (" 3) Intializing matrix data with random number range from 0 to 1.\n\n");
  Initdata_cpu(A, x, y, m, n);
  naive_impl(A, x, ynaive, m, n);
  printf (" 4) Finish init, start to test, nruns is %d warmup is 10 rounds. \n\n", nruns);

  double *timestat = (double*)malloc(sizeof(double)*nruns);
  double *presstat = (double*)malloc(sizeof(double)*nruns);
  double *bandwithstat = (double*)malloc(sizeof(double)*nruns);


/**
 * @brief gemv various interface.
 * 
 */
#ifdef USE_INTEL  
for(int nr=0; nr<nruns+warmup; nr++){
  double stime = gettime();
#ifdef USE_DOUBLE
  cblas_dgemv(CblasColMajor, CblasNoTrans, 
    m, n, alpha, A, m, x, 1, beta, y, 1);
#else 
  cblas_sgemv(CblasColMajor, CblasNoTrans, 
    m, n, alpha, A, m, x, 1, beta, y, 1);
#endif 
  double etime = gettime();
  if(nr < warmup) continue;
  timestat[nr-warmup] = etime - stime;
  presstat[nr-warmup] = checkcorrectness(y,ynaive, m,n);
}
#endif 

#ifdef USE_NVIDIA
for(int nr=0; nr<nruns+warmup; nr++){
  float cpytime = 0.0, executime = 0.0, time = 0.0;
  cudaEventRecord(start, 0);
  cudaMemcpy(d_A, A, m * n * sizeof(real_t), cudaMemcpyDefault);
  cudaMemcpy(d_x, x, n * sizeof(real_t), cudaMemcpyDefault);
  cudaMemcpy(d_y, y, m * sizeof(real_t), cudaMemcpyDefault);
  cudaEventRecord(stop, 0);
  cudaDeviceSynchronize();
  time = 0.0;
  cudaEventElapsedTime(&time, start, stop);
  cpytime += time;
  cudaEventRecord(start, 0);
#ifdef USE_DOUBLE
  cublasDgemv(handle, CUBLAS_OP_N, m, n, &alpha, d_A, m, d_x, 1, &beta, d_y, 1);
#else 
  cublasSgemv(handle, CUBLAS_OP_N, m, n, &alpha, d_A, m, d_x, 1, &beta, d_y, 1);
#endif 
  cudaEventRecord(stop, 0);
  cudaEventSynchronize(stop);
  time = 0.0;
  cudaEventElapsedTime(&time, start, stop);
  executime += time;
  cudaEventRecord(start, 0);
  cudaMemcpy(A, d_A, m * n * sizeof(real_t), cudaMemcpyDefault);
  cudaMemcpy(x, d_x, n * sizeof(real_t), cudaMemcpyDefault);
  cudaMemcpy(y, d_y, m * sizeof(real_t), cudaMemcpyDefault);
  cudaEventRecord(stop, 0);
  cudaDeviceSynchronize();
  time = 0.0;
  cudaEventElapsedTime(&time, start, stop);
  cpytime += time;
  if(nr < warmup) continue;
  timestat[nr-warmup] = executime;
  presstat[nr-warmup] = checkcorrectness(y,ynaive, m,n);
  bandwithstat[nr-warmup] =  sizeof(real_t) * (m * n + m + n) * 2 / (cpytime * 1e-3 * 1073741824.) ;
}
#endif




/**
 * @brief free space and write to file
 * 
 */
#ifdef USE_INTEL
  
  mkl_free(A);
  mkl_free(x);
  mkl_free(y);
  double timemean = mean(timestat, nruns);
  double timevar = var(timestat, nruns);
  csort(timestat, nruns);
  double time50th = getquatile(timestat, 0.5, nruns);
  double time25th = getquatile(timestat, 0.25, nruns);
  double time75th = getquatile(timestat, 0.75, nruns);
  double timemax = timestat[nruns-1];
  double timemin = timestat[0];
  double presmean = mean(presstat, nruns);
  saveresults(m,n,timemax, timemin, time50th, time25th, time75th, presmean, 0, exptype, filepath);
  printf (" 5) quick look at the test time mean (seconds) and var %.3e, %.3e. \n\n", timemean, timevar);
  printf (" 6) Deallocating memory and write results to files. \n\n");
#endif

#ifdef USE_NVIDIA
  free(A);
  free(x);
  free(y);
  cudaFree(d_A);
  cudaFree(d_x);
  cudaFree(d_y);
  double timemean = mean(timestat, nruns);
  double timevar = var(timestat, nruns);
  csort(timestat, nruns);
  double time50th = getquatile(timestat, 0.5, nruns);
  double time25th = getquatile(timestat, 0.25, nruns);
  double time75th = getquatile(timestat, 0.75, nruns);
  double timemax = timestat[nruns-1];
  double timemin = timestat[0];
  double presmean = mean(presstat, nruns);
  double bandmean = mean(bandwithstat, nruns);
  saveresults(m,n,timemax, timemin, time50th, time25th, time75th, presmean, bandmean, exptype, filepath);
  printf (" 5) quick look at the test time mean and var %.3e, %.3e. \n\n", timemean, timevar);
  printf (" 6) Deallocating memory and write results to files. \n\n");
#endif 


  free(timestat);
  free(presstat);
  free(bandwithstat);
  return 0;
}