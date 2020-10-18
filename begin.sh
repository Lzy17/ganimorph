#!/usr/bin/env bash

#SBATCH --job-name=cyclegan
#SBATCH --account=sds173
#SBATCH --partition=gpu
#SBATCH --nodes=8
#SBATCH --ntasks-per-node=24
#SBATCH --gres=gpu:4
#SBATCH --time=04:00:00
#SBATCH --output=tf-gpu.o%j.%N

module purge
module list
printenv

time -p singularity exec --bind /oasis --nv /share/apps/gpu/singularity/images/tensorflow/tensorflow-v1.15.2-gpu-20200318.simg python3 main.py --data /home/joeyli/projects/cyclegan/pytorch-CycleGAN-and-pix2pix/datasets/maps --batch_size 16 

