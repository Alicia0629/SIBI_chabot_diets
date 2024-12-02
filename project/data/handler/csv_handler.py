import pandas as pd
import os
from tqdm import tqdm

class CSVHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        self.recipes = self.load_dataset(file_path)

    def get_dataset(self):
        """
        Get dataset in self.recipes.
        :return: DataFrame with recipes.
        """
        return self.recipes

    def load_dataset(self, file_path):
        """
        Load dataset from a csv file.
        :return: DataFrame with recipes.
        """

        for root, dirs, files in os.walk('..'):
            if file_path in files:
                file_path = os.path.join(root, file_path)
                break

        total_rows = sum(1 for _ in open(file_path)) - 1
        chunk_size=total_rows//50 + 1

        chunks = []
        with tqdm(total=total_rows, desc="Loading CSV") as pbar:
            for chunk in pd.read_csv(file_path, chunksize=chunk_size):
                chunks.append(chunk)
                pbar.update(len(chunk))

        self.recipes = pd.concat(chunks, ignore_index=True)
        return self.recipes

    def filter_recipes(self, filters):
        """
        Returns a DataFrame filtered based on dietary restrictions.
        :param  filters: Dictionary with allergies. It must include the following keys: HasDairy,HasGluten,HasEgg,HasFish,HasShellfish,HasTreenut,HasPeanut,HasSoy,HasSesame,HasMustard

        :return: DataFrame filtered.
        """
        filtered = self.recipes
        for key, value in filters.items():
            if key in filtered.columns:
                filtered = filtered[filtered[key] == value]

        return filtered

    def get_recipe_details(self, recipe_id):
        """
        Return details of a recipe.
        :param recipe_id: ID of recipe.
        :return: Dictionary with details of the recipe.
        """

        recipe = self.recipes[self.recipes['RecipeId'] == recipe_id]
        if recipe.empty:
            return None
        return recipe.iloc[0].to_dict()


