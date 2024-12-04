#!/bin/sh

cd conda-env
bash loadEnvironment.sh
source ~/anaconda3/bin/activate diet-recommender
conda activate diet-recommender
cd ..

cd data/prep_scripts
bash main.sh
cd ../..
