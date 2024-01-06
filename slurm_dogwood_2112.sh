#!/bin/bash
#SBATCH -p 2112_queue
#SBATCH -J skmNd20
#SBATCH -o out_%A.out
#SBATCH -N 13
#SBATCH --ntasks-per-node=44 
#SBATCH --time=02-00:00:00   #format days-hh:mm:ss

ulimit -s unlimited
mpirun ./run_pynfam.py


