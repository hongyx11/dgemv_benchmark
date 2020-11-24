#!/bin/bash
#SBATCH --job-name=v100
#SBATCH -N 1
#SBATCH --partition=batch
#SBATCH --output=log/job.%J.out
#SBATCH --error=log/job.%J.err
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=yuxi.hong@kaust.edu.sa
#SBATCH --time=1:00:00
#SBATCH --mem=64G
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=6
#SBATCH --constraint=[v100]
module load gcc/8.2.0
module load cuda/11.0.1
./bin/nvidiasingle.out fixed 1000 100 10 v100 res.txt
