import kagglehub
import os
import shutil

path = kagglehub.dataset_download("irkaal/foodcom-recipes-and-reviews")

destination_folder = os.path.join('data', 'datasets')

shutil.move(path, destination_folder)

