#!/bin/bash

export CUDA_VISIBLE_DEVICES=$2
make nvidia
GPUTYPE=$1

if [ -z "$GPUTYPE" ]
then 
echo "GPUTYPE not set. please try agin."
exit
fi

if [ -z "$CUDA_VISIBLE_DEVICES" ]
then 
echo "CUDA_VISIBLE_DEVICES not set. please try agin."
exit
fi

# transpose
./bin/nvidiasingle_transpose fixed 10000 5000 1000 ${GPUTYPE} 
./bin/nvidiasingle_transpose fixed 20000 5000 1000 ${GPUTYPE} 
./bin/nvidiasingle_transpose fixed 25000 5000 1000 ${GPUTYPE} 
./bin/nvidiasingle_transpose fixed 80000 8000 1000 ${GPUTYPE} 
# ./bin/nvidiasingle_transpose fixed 70000 35000 1000 ${GPUTYPE} 

# transpose
./bin/nvidiadouble_transpose fixed 10000 5000 1000 ${GPUTYPE} 
./bin/nvidiadouble_transpose fixed 20000 5000 1000 ${GPUTYPE} 
./bin/nvidiadouble_transpose fixed 25000 5000 1000 ${GPUTYPE} 
./bin/nvidiadouble_transpose fixed 80000 8000 1000 ${GPUTYPE} 
# ./bin/nvidiadouble_transpose fixed 70000 35000 1000 ${GPUTYPE} 
