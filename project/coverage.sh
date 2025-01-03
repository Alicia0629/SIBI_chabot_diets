#!/bin/bash

eval "$(conda shell.bash hook)"
conda activate diet-recommender

export PYTHONPATH=$(pwd):$PYTHONPATH

coverage run -m pytest
coverage report
coverage html

google-chrome htmlcov/index.html

