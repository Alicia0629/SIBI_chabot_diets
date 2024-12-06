#!/bin/bash

eval "$(conda shell.bash hook)"
conda activate diet-recommender

export PYTHONPATH=$(pwd):$PYTHONPATH

streamlit run ui/web.py
