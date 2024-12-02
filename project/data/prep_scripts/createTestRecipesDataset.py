import sys
import os
import pandas

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from handler.csv_handler import CSVHandler

csv_original = "../datasets/NewRecipes.csv"
csv_output = "../datasets/TestRecipes.csv"

recipes = CSVHandler(csv_original).get_dataset()
recipesOutput = recipes.head(10)

recipesOutput.to_csv(csv_output, index=False)
