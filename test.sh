#!/usr/bin/env bash
#SBATCH --job-name=cyclegan
#SBATCH --account=sds173
#SBATCH --partition=gpu-shared
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=6
#SBATCH --gres=gpu:1
#SBATCH --time=00:01:00
#SBATCH --output=pytorch-gpu-shared.o%j.%N


module purge
module list
printenv

time -p singularity exec --bind /oasis --nv /share/apps/gpu/singularity/images/pytorch/pytorch-v1.5.0-gpu-20200511.simg python3 test.py --dataroot ./datasets/maps --name maps_cyclegan --model cycle_gan
