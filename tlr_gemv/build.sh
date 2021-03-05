#!/bin/bash
#

source /usr/uhome/aurora/mpc/pub/NECmpi.dir/2.13.0/bin/necmpivars.sh
source /opt/nec/ve/nlc/2.1.0/bin/nlcvars.sh

mpincc -O3 dgemv.c -DUSE_NEC -o necsingle -lcblas -fopenmp -lblas_sequential

exit 0
