#BLAS_DIR=/home/ltaiefh/bench/blis/install
BLAS_DIR=/home/ltaiefh/codes/kblas-cpu-amd/amd-blis
CC=gcc -std=gnu99
NVCC=nvcc

intel:
	mkdir -p bin
	mkdir -p log
	mkdir -p plots
	${CC} -O3 dgemv.c  \
	-DUSE_INTEL -DUSE_DOUBLE \
	-DMKL_ILP64 -m64 -I${MKL_ROOT}/include \
	-o bin/inteldouble \
	-Wl,--start-group ${MKL_ROOT}/lib/intel64/libmkl_intel_ilp64.a \
	${MKL_ROOT}/lib/intel64/libmkl_gnu_thread.a ${MKL_ROOT}/lib/intel64/libmkl_core.a \
	-Wl,--end-group -lgomp -lpthread -lm -ldl

	${CC} -O3 dgemv.c \
	-DUSE_INTEL \
	-DMKL_ILP64 -m64 -I${MKL_ROOT}/include \
	-o bin/intelsingle \
	-Wl,--start-group ${MKL_ROOT}/lib/intel64/libmkl_intel_ilp64.a \
	${MKL_ROOT}/lib/intel64/libmkl_gnu_thread.a ${MKL_ROOT}/lib/intel64/libmkl_core.a \
	-Wl,--end-group -lgomp -lpthread -lm -ldl

	${CC} -O3 dgemv_transpose.c  \
	-DUSE_INTEL -DUSE_DOUBLE \
	-DMKL_ILP64 -m64 -I${MKL_ROOT}/include \
	-o bin/inteldouble_transpose \
	-Wl,--start-group ${MKL_ROOT}/lib/intel64/libmkl_intel_ilp64.a \
	${MKL_ROOT}/lib/intel64/libmkl_gnu_thread.a ${MKL_ROOT}/lib/intel64/libmkl_core.a \
	-Wl,--end-group -lgomp -lpthread -lm -ldl

	${CC} -O3 dgemv_transpose.c \
	-DUSE_INTEL \
	-DMKL_ILP64 -m64 -I${MKL_ROOT}/include \
	-o bin/intelsingle_transpose \
	-Wl,--start-group ${MKL_ROOT}/lib/intel64/libmkl_intel_ilp64.a \
	${MKL_ROOT}/lib/intel64/libmkl_gnu_thread.a ${MKL_ROOT}/lib/intel64/libmkl_core.a \
	-Wl,--end-group -lgomp -lpthread -lm -ldl


nec:
	. /opt/nec/ve/nlc/2.1.0/bin/nlcvars.sh
	mkdir -p bin
	mkdir -p log
	mkdir -p plots
	ncc -O3 dgemv.c  \
	-DUSE_NEC -DUSE_DOUBLE \
	-o bin/necdouble \
	-lcblas -fopenmp -lblas_openmp

	ncc -O3 dgemv.c \
	-DUSE_NEC \
	-o bin/necsingle \
	-lcblas -fopenmp -lblas_openmp

	ncc -O3 dgemv_transpose.c  \
	-DUSE_NEC -DUSE_DOUBLE \
	-o bin/necdouble_transpose \
	-lcblas -fopenmp -lblas_openmp

	ncc -O3 dgemv_transpose.c \
	-DUSE_NEC \
	-o bin/necsingle_transpose \
	-lcblas -fopenmp -lblas_openmp


nvidia:
	mkdir -p bin
	mkdir -p log
	mkdir -p plots
	${NVCC} -O3 dgemv.c \
	-DUSE_NVIDIA -DUSE_DOUBLE \
	-o bin/nvidiadouble \
	-I${CUDAROOT}/include -L${CUDAROOT}/lib64 -lcublas -lcudart 

	${NVCC} -g -O3 dgemv.c \
	-DUSE_NVIDIA \
	-o bin/nvidiasingle \
	-I${CUDAROOT}/include -L${CUDAROOT}/lib64 -lcublas -lcudart 

	${NVCC} -O3 dgemv_transpose.c \
	-DUSE_NVIDIA -DUSE_DOUBLE \
	-o bin/nvidiadouble_transpose \
	-I${CUDAROOT}/include -L${CUDAROOT}/lib64 -lcublas -lcudart 

	${NVCC} -g -O3 dgemv_transpose.c \
	-DUSE_NVIDIA \
	-o bin/nvidiasingle_transpose \
	-I${CUDAROOT}/include -L${CUDAROOT}/lib64 -lcublas -lcudart 

amd:
	mkdir -p bin
	mkdir -p log
	mkdir -p plots
	${CC} -O3 -fopenmp dgemv.c  \
	-DUSE_AMD -DUSE_DOUBLE -I${BLAS_DIR}/include \
	-o bin/amddouble -L${BLAS_DIR}/lib \
	-lblis-mt -lgomp -lpthread -lm -ldl

	${CC} -O3 -fopenmp dgemv.c \
	-DUSE_AMD -I${BLAS_DIR}/include \
	-o bin/amdsingle -L${BLAS_DIR}/lib \
	-lblis-mt -lgomp -lpthread -lm -ldl

	${CC} -O3 -fopenmp dgemv_transpose.c  \
	-DUSE_AMD -DUSE_DOUBLE -I${BLAS_DIR}/include \
	-o bin/amddouble_transpose -L${BLAS_DIR}/lib \
	-lblis-mt -lgomp -lpthread -lm -ldl

	${CC} -O3 -fopenmp dgemv_transpose.c \
	-DUSE_AMD -I${BLAS_DIR}/include \
	-o bin/amdsingle_transpose -L${BLAS_DIR}/lib \
	-lblis-mt -lgomp -lpthread -lm -ldl

all: intel nvidia amd nec
