import pandas as pd
from tqdm import tqdm

class CSVHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        load_dataset(file_path)

    def load_dataset(file_path):
        """
        Load dataset from a csv file.
        :return: DataFrame with recipes.
        """
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
            if value in filtered.columns:
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


