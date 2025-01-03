import sys
import os
import pandas

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from handler.csv_handler import CSVHandler

csv_original = "../datasets/NewRecipes.csv"
csv_output = "../datasets/TestRecipes.csv"
csv_output2 = "../datasets/TestRecipes2.csv"

recipes = CSVHandler(csv_original).get_dataset()

recipesOutput = recipes.head(10)
recipesOutput.to_csv(csv_output, index=False)

recipesOutput2 = recipesOutput.head(2)
recipesOutput2.to_csv(csv_output2, index=False)