import pytest
import pandas as pd
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from data.handler.csv_handler import CSVHandler

@pytest.fixture
def sample_csv_data():
    return "TestRecipes.csv"

def test_load_csv(sample_csv_data):
    handler = CSVHandler(sample_csv_data)
    data = handler.get_dataset()
    assert len(data) > 0, "The CSV file should not be empty"
    assert "RecipeId" in data.columns, "The CSV file should contain the 'RecipeId' column"

def test_filter_recipes_by_allergen1(sample_csv_data):
    handler = CSVHandler(sample_csv_data)
    recipes = handler.get_dataset()

    filters = {"HasDairy": False}
    filtered_recipes = handler.filter_recipes(filters)

    assert all(filtered_recipes["HasDairy"]==False), "All filtered recipes should not have dairy"



def test_filter_recipes_by_allergen2(sample_csv_data):
    handler = CSVHandler(sample_csv_data)
    recipes = handler.get_dataset()

    filters = {"HasDairy": False, "HasEgg": False}
    filtered_recipes = handler.filter_recipes(filters)

    assert all(filtered_recipes["HasDairy"]==False), "All filtered recipes should not have dairy"
    assert all(filtered_recipes["HasEgg"]==False), "All filtered recipes should not have egg"

def test_filter_recipes_by_allergen3(sample_csv_data):
    handler = CSVHandler(sample_csv_data)
    recipes = handler.get_dataset()

    filters = {"HasDairy": True}
    filtered_recipes = handler.filter_recipes(filters)

    assert all(filtered_recipes["HasDairy"]), "All filtered recipes should have dairy"


def test_get_recipe_by_id(sample_csv_data):
    handler = CSVHandler(sample_csv_data)
    recipe = handler.get_recipe_details(38)
    assert recipe["Name"] == "Low-Fat Berry Blue Frozen Dessert", "The recipe name should match the expected value"

