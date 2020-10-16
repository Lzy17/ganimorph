#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: GANimorph.py
# Author: Aaron Gokaslan (agokasla@cs.brown.edu)

import cv2
import os, sys
import argparse
from six.moves import map, zip
import numpy as np
from glob import glob

from model import Model
from tensorpack import *
from tensorpack.utils.viz import *
import tensorpack.tfutils.symbolic_functions as symbf
from tensorpack.tfutils.summary import add_moving_summary
import tensorflow as tf
from tensorflow.python.training import moving_averages
from utils import *
from GAN import GANTrainer, SeparateGANTrainer, GANModelDesc
"""
The official code for Improved Shape Deformation in Unsupervised Image to Image
Translation.

Requires Tensorpack and related dependencies.

author: Aaron Gokaslan agokasla@cs.brown.edu
"""

parser = argparse.ArgumentParser()
parser.add_argument(
    '--data', required=True,
    help='the img_align_celeba directory. should also contain list_attr_celeba.txt')
parser.add_argument('--load', help='load model')
args = parser.parse_args()

if __name__ == '__main__':
    logger.auto_set_dir()
    data = get_data(args.data)
    data = QueueInput(data)
    # train 1 D after 2 G




    trainer = GANTrainer(data, Model(), get_num_gpu())
    trainer.train_with_defaults(
        callbacks=[
            PeriodicTrigger(ModelSaver(), every_k_epochs=20),
            PeriodicTrigger(VisualizeTestSet(args.data), every_k_epochs=3),
            ScheduledHyperParamSetter(
                                'learning_rate',
                                [(150, 2e-4), (300, 0)], interp='linear')],
        steps_per_epoch=1000,
        session_init=SaverRestore(args.load) if args.load else None
    )
