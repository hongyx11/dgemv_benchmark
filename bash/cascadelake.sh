#!/bin/bash
# SBATCH --job-name=csc
# SBATCH -N 1
# SBATCH --partition=batch
# SBATCH --output=log/job.%J.out
# SBATCH --error=log/job.%J.out
# SBATCH --cpus-per-task=40
# SBATCH --mail-type=END,FAIL
# SBATCH --mail-user=yuxi.hong@kaust.edu.sa
#SBATCH --time=1:00:00
# SBATCH --threads-per-core=1
# SBATCH --hint=nomultithread
# SBATCH --constraint=cascadelake
module load gcc/8.2.0
module load intel/2020
echo "Working Dir is $(pwd)" 
source /home/hongy0a/dgemv_benchmark/bash/intel.sh cascadelake
source /home/hongy0a/dgemv_benchmark/bash/intel_transpose.sh cascadelake
