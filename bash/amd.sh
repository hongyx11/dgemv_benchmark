#!/bin/bash
make amd
CPUTYPE=$1

if [ -z "$CPUTYPE" ]
then 
echo "CPUTYPE not set. please try agin."
exit
fi

# no transpose 
OMP_PLACES=cores BLIS_NUM_THREADS=128 ./bin/amdsingle fixed 5000 10000 1000 ${CPUTYPE} 
OMP_PLACES=cores BLIS_NUM_THREADS=128 ./bin/amdsingle fixed 5000 20000 1000 ${CPUTYPE}
OMP_PLACES=cores BLIS_NUM_THREADS=128 ./bin/amdsingle fixed 2000 10000 1000 ${CPUTYPE} 
OMP_PLACES=cores BLIS_NUM_THREADS=128 ./bin/amdsingle fixed 5000 25000 1000 ${CPUTYPE} 
OMP_PLACES=cores BLIS_NUM_THREADS=128 ./bin/amdsingle fixed 8000 80000 1000 ${CPUTYPE} 
OMP_PLACES=cores BLIS_NUM_THREADS=128 ./bin/amdsingle fixed 35000 70000 1000 ${CPUTYPE} 

# no transpose 
OMP_PLACES=cores BLIS_NUM_THREADS=128 ./bin/amddouble fixed 5000 10000 1000 ${CPUTYPE} 
OMP_PLACES=cores BLIS_NUM_THREADS=128 ./bin/amddouble fixed 5000 20000 1000 ${CPUTYPE} 
OMP_PLACES=cores BLIS_NUM_THREADS=128 ./bin/amddouble fixed 2000 10000 1000 ${CPUTYPE} 
OMP_PLACES=cores BLIS_NUM_THREADS=128 ./bin/amddouble fixed 5000 25000 1000 ${CPUTYPE} 
OMP_PLACES=cores BLIS_NUM_THREADS=128 ./bin/amddouble fixed 8000 80000 1000 ${CPUTYPE} 
OMP_PLACES=cores BLIS_NUM_THREADS=128 ./bin/amddouble fixed 35000 70000 1000 ${CPUTYPE} 

