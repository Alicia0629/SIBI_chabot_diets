import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from tqdm import tqdm
import ast

print("Searching datasets...")

dataset_dir = os.path.join('..','datasets')
recipes_path = ""
allergies_path = ""
path = ""

for root, dirs, files in os.walk(dataset_dir):
    if 'recipes.csv' in files:
        recipes_path = os.path.join(root, 'recipes.csv')
    if 'Allergies.csv' in files:
        path = root
        allergies_path = os.path.join(root, 'Allergies.csv')

def load_dataset(file_path):
    total_rows = sum(1 for _ in open(file_path)) - 1
    chunk_size=total_rows//50 + 1

    chunks = []
    with tqdm(total=total_rows, desc="Loading CSV") as pbar:
        for chunk in pd.read_csv(file_path, chunksize=chunk_size):
            chunks.append(chunk)
            pbar.update(len(chunk))

    return pd.concat(chunks, ignore_index=True)

print("Opening recipes dataset...")
datasetRecipes = load_dataset(recipes_path)

print("Opening allergies dataset...")
datasetAllergies = load_dataset(allergies_path)

colIngredients = "RecipeIngredientParts"

#Cleanning ingredients columns
print("Cleanning column "+colIngredients+"...")
tqdm.pandas()

def convert_string_to_list(string):
    stringlist=[]
    if string.startswith('c("'):
        string="["+string[2:-1]+"]"
        stringlist=ast.literal_eval(string)
    elif string.startswith('"'):
        stringlist.append(string[1:-1])
    return stringlist

colIngredients = "RecipeIngredientParts"
datasetRecipes[colIngredients] = datasetRecipes[colIngredients].progress_apply(convert_string_to_list)

#Creating HasAllergy columns

print("Creating HasALlergy columns...")

def createColumns(data, positiveTerms, negativeTerms):
    def contains_any_term(ingredients):
        for ingredient in ingredients:
            ingredient = ingredient.lower()
            for term in positiveTerms:
                if term in ingredient:
                    positive = True
                    for negativeTerm in negativeTerms:
                        if negativeTerm in ingredient:
                            positive = False
                            break
                    if positive:
                        return True
        return False

    return data[colIngredients].apply(contains_any_term)


for index, row in tqdm(datasetAllergies.iterrows(), total=datasetAllergies.shape[0]):
    trueAllergy = ast.literal_eval(row["trueAllergy"]) if isinstance(row["trueAllergy"], str) else row["trueAllergy"]
    falseAllergy = ast.literal_eval(row["falseAllergy"]) if isinstance(row["falseAllergy"], str) else row["falseAllergy"]
    
    datasetRecipes["Has" + row["Allergy"]] = createColumns(datasetRecipes, trueAllergy, falseAllergy)


datasetRecipes.to_csv(os.path.join(path, 'NewRecipes.csv'))


