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

###########################################################################

# MICADO [1] instrument
# no transpose 
./bin/nvidiasingle fixed 5000 10000 1000 ${GPUTYPE}  # Dimension for 1 GPU
./bin/nvidiasingle fixed 2500 10000 1000 ${GPUTYPE}  # Dimension for 2 GPUs
./bin/nvidiasingle fixed 1250 10000 1000 ${GPUTYPE}  # Dimension for 4 GPUs
./bin/nvidiasingle fixed 625 10000 1000 ${GPUTYPE}  # Dimension for 8 GPUs

./bin/nvidiadouble fixed 5000 10000 1000 ${GPUTYPE} # Dimension for 1 GPU
./bin/nvidiadouble fixed 2500 10000 1000 ${GPUTYPE} # Dimension for 2 GPUs
./bin/nvidiadouble fixed 1250 10000 1000 ${GPUTYPE} # Dimension for 4 GPUs 
./bin/nvidiadouble fixed 625 10000 1000 ${GPUTYPE} # Dimension for 8 GPUs

###########################################################################

# MAVIS instrument
# no transpose 
./bin/nvidiasingle fixed 5000 20000 1000 ${GPUTYPE} # Dimension for 1 GPU
./bin/nvidiasingle fixed 2500 20000 1000 ${GPUTYPE} # Dimension for 2 GPUs
./bin/nvidiasingle fixed 1250 20000 1000 ${GPUTYPE} # Dimension for 4 GPUs
./bin/nvidiasingle fixed 625 20000 1000 ${GPUTYPE} # Dimension for 8 GPUs

./bin/nvidiadouble fixed 5000 20000 1000 ${GPUTYPE} # Dimension for 1 GPU
./bin/nvidiadouble fixed 2500 20000 1000 ${GPUTYPE} # Dimension for 2 GPUs
./bin/nvidiadouble fixed 1250 20000 1000 ${GPUTYPE} # Dimension for 4 GPUs
./bin/nvidiadouble fixed 625 20000 1000 ${GPUTYPE} # Dimension for 8 GPUs

###########################################################################

# SCEXAO instrument
# no transpose 
./bin/nvidiasingle fixed 2000 10000 1000 ${GPUTYPE} # Dimension for 1 GPU
./bin/nvidiasingle fixed 1000 10000 1000 ${GPUTYPE} # Dimension for 2 GPUs
./bin/nvidiasingle fixed 500 10000 1000 ${GPUTYPE} # Dimension for 4 GPUs
./bin/nvidiasingle fixed 200 10000 1000 ${GPUTYPE} # Dimension for 8 GPUs

./bin/nvidiadouble fixed 2000 10000 1000 ${GPUTYPE} # Dimension for 1 GPU
./bin/nvidiadouble fixed 1000 10000 1000 ${GPUTYPE} # Dimension for 2 GPUs
./bin/nvidiadouble fixed 500 10000 1000 ${GPUTYPE} # Dimension for 4 GPUs
./bin/nvidiadouble fixed 200 10000 1000 ${GPUTYPE} # Dimension for 8 GPUs

###########################################################################

# SCEXAO instrument
# no transpose 
./bin/nvidiasingle fixed 2000 14000 1000 ${GPUTYPE} # Dimension for 1 GPU
./bin/nvidiasingle fixed 1000 14000 1000 ${GPUTYPE} # Dimension for 2 GPUs
./bin/nvidiasingle fixed 500 14000 1000 ${GPUTYPE} # Dimension for 4 GPUs
./bin/nvidiasingle fixed 200 14000 1000 ${GPUTYPE} # Dimension for 8 GPUs

./bin/nvidiadouble fixed 2000 14000 1000 ${GPUTYPE} # Dimension for 1 GPU
./bin/nvidiadouble fixed 1000 14000 1000 ${GPUTYPE} # Dimension for 2 GPUs
./bin/nvidiadouble fixed 500 14000 1000 ${GPUTYPE} # Dimension for 4 GPUs
./bin/nvidiadouble fixed 200 14000 1000 ${GPUTYPE} # Dimension for 8 GPUs

###########################################################################

# MICADO [2] instrument
# no transpose 
./bin/nvidiasingle fixed 5000 25000 1000 ${GPUTYPE} # Dimension for 1 GPU
./bin/nvidiasingle fixed 2500 25000 1000 ${GPUTYPE}  # Dimension for 2 GPUs
./bin/nvidiasingle fixed 1250 25000 1000 ${GPUTYPE}  # Dimension for 4 GPUs
./bin/nvidiasingle fixed 625 25000 1000 ${GPUTYPE}  # Dimension for 8 GPUs

./bin/nvidiadouble fixed 5000 25000 1000 ${GPUTYPE} # Dimension for 1 GPU
./bin/nvidiadouble fixed 2500 25000 1000 ${GPUTYPE}  # Dimension for 2 GPUs
./bin/nvidiadouble fixed 1250 25000 1000 ${GPUTYPE}  # Dimension for 4 GPUs
./bin/nvidiadouble fixed 625 25000 1000 ${GPUTYPE}  # Dimension for 8 GPUs

###########################################################################

# MAORY instrument
# no transpose 
./bin/nvidiasingle fixed 8000 80000 1000 ${GPUTYPE} # Dimension for 1 GPU
./bin/nvidiasingle fixed 4000 80000 1000 ${GPUTYPE} # Dimension for 2 GPUs
./bin/nvidiasingle fixed 2000 80000 1000 ${GPUTYPE} # Dimension for 4 GPUs
./bin/nvidiasingle fixed 1000 80000 1000 ${GPUTYPE} # Dimension for 8 GPUs

./bin/nvidiadouble fixed 8000 80000 1000 ${GPUTYPE} # Dimension for 1 GPU
./bin/nvidiadouble fixed 4000 80000 1000 ${GPUTYPE} # Dimension for 2 GPUs
./bin/nvidiadouble fixed 2000 80000 1000 ${GPUTYPE} # Dimension for 4 GPUs
./bin/nvidiadouble fixed 1000 80000 1000 ${GPUTYPE} # Dimension for 8 GPUs

###########################################################################

# EPICS instrument
# no transpose 
./bin/nvidiasingle fixed 35000 70000 1000 ${GPUTYPE} # Dimension for 1 GPU
./bin/nvidiasingle fixed 17500 70000 1000 ${GPUTYPE} # Dimension for 2 GPUs
./bin/nvidiasingle fixed 8750 70000 1000 ${GPUTYPE} # Dimension for 4 GPUs
./bin/nvidiasingle fixed 4375 70000 1000 ${GPUTYPE} # Dimension for 8 GPUs

./bin/nvidiadouble fixed 35000 70000 1000 ${GPUTYPE} # Dimension for 1 GPU
./bin/nvidiadouble fixed 17500 70000 1000 ${GPUTYPE} # Dimension for 2 GPUs
./bin/nvidiadouble fixed 8750 70000 1000 ${GPUTYPE} # Dimension for 4 GPUs
./bin/nvidiadouble fixed 4375 70000 1000 ${GPUTYPE} # Dimension for 8 GPUs

###########################################################################
