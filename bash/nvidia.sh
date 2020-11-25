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

# no transpose 
./bin/nvidiasingle fixed 5000 10000 100 ${GPUTYPE} 
./bin/nvidiasingle fixed 5000 20000 100 ${GPUTYPE} 
./bin/nvidiasingle fixed 5000 25000 100 ${GPUTYPE} 
./bin/nvidiasingle fixed 8000 80000 100 ${GPUTYPE} 
# ./bin/nvidiasingle fixed 35000 70000 100 ${GPUTYPE} 

# no transpose 
./bin/nvidiadouble fixed 5000 10000 100 ${GPUTYPE} 
./bin/nvidiadouble fixed 5000 20000 100 ${GPUTYPE} 
./bin/nvidiadouble fixed 5000 25000 100 ${GPUTYPE} 
./bin/nvidiadouble fixed 8000 80000 100 ${GPUTYPE} 
# ./bin/nvidiadouble fixed 35000 70000 100 ${GPUTYPE} 
