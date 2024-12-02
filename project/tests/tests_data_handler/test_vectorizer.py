import pytest
import pandas as pd
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from data.handler.vectorizer import Vectorizer
from data.handler.csv_handler import CSVHandler


@pytest.fixture
def sample_recipes():
    return CSVHandler("TestRecipes.csv").get_dataset()

def test_initialize_vectorizer(sample_recipes):
    vectorizer = Vectorizer(sample_recipes)
    assert vectorizer, "The vectorizer should initialize correctly"

def test_build_index_vectorizer(sample_recipes):
    vectorizer = Vectorizer(sample_recipes)
    assert vectorizer.index is not None, "The index should be built correctly"

def test_search_returns_correct_type(sample_recipes):
    vectorizer = Vectorizer(sample_recipes)
    result = vectorizer.search("chicken", k=2)
    assert isinstance(result, pd.DataFrame)

def test_search_returns_k_results(sample_recipes):
    vectorizer = Vectorizer(sample_recipes)
    result = vectorizer.search("berry", k=1)
    assert len(result) == 1

def test_search_with_different_k(sample_recipes):
    vectorizer = Vectorizer(sample_recipes)
    result = vectorizer.search("dessert", k=3)
    assert len(result) == 3

