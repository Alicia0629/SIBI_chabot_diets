#!/bin/bash

eval "$(conda shell.bash hook)"
conda activate diet-recommender

export PYTHONPATH=$(pwd):$PYTHONPATH

python3 tests/run_tests.py
