#!/bin/sh

source ~/anaconda3/etc/profile.d/conda.sh
conda activate diet-recommender
conda env export > environment.yml
