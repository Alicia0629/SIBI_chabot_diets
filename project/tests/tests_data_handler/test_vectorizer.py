import pytest
import pandas as pd
import sys
import os
import pickle
import numpy as np
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

# Test for no embeddings found, triggering the index regeneration
def test_no_embeddings_found_and_index_regenerated(sample_recipes):
    # Simulate the scenario where the embeddings file does not exist or is invalid
    vectorizer = Vectorizer(sample_recipes, embeddings_file="tests/data/invalid_embeddings.pkl")
    # Check if the index is generated after the failed embedding loading
    assert vectorizer.index is not None, "The FAISS index should be built after embeddings fail to load."

# Test for embeddings file not found, triggering the index generation
def test_embeddings_file_not_found(sample_recipes):
    # Simulate the scenario where the embeddings file does not exist
    vectorizer = Vectorizer(sample_recipes, embeddings_file="tests/data/non_existent_embeddings.pkl")
    # Check if the index is generated
    assert vectorizer.index is not None, "The FAISS index should be built when embeddings file is not found."

# Test for successfully building the index after generating embeddings
def test_successful_index_building(sample_recipes):
    # Mock the behavior to simulate building of embeddings and index creation
    vectorizer = Vectorizer(sample_recipes)
    # Check if the index is built successfully
    assert vectorizer.index is not None, "The FAISS index should be built when embeddings are generated."

# Test for empty embeddings, triggering index regeneration
def test_empty_embeddings_triggers_index_generation(sample_recipes):
    # Simulate a scenario where embeddings file has an empty array
    vectorizer = Vectorizer(sample_recipes, embeddings_file="tests/data/empty_embeddings.pkl")
    # Check if the embeddings file is empty and index is rebuilt
    assert vectorizer.index is not None, "The FAISS index should be rebuilt when embeddings are empty."
    
# Test for FAISS index search failure if index is not initialized
def test_faiss_search_when_index_not_initialized(sample_recipes):
    vectorizer = Vectorizer(sample_recipes)
    # Set index to None to simulate uninitialized index
    vectorizer.index = None
    try:
        vectorizer.search("chicken", k=2)
    except Exception as e:
        assert str(e) == "FAISS index has not been initialized.", "Should raise an exception when FAISS index is not initialized."

# Test for case when embeddings file is not found and index is generated
def test_embeddings_file_not_found_generating_embeddings(sample_recipes):
    # Simulate the scenario where the embeddings file does not exist
    vectorizer = Vectorizer(sample_recipes, embeddings_file="tests/data/non_existent_embeddings.pkl")
    
    # Check if the index is built (this is done in the build_index method)
    assert vectorizer.index is not None, "The FAISS index should be built when embeddings file is not found."

    # Check if embeddings were generated
    assert vectorizer.embeddings is not None and vectorizer.embeddings.size > 0, "Embeddings should be generated when file is not found."

# Test for case empty embbedings
def test_embeddings_empty_and_regenerating(sample_recipes):
    # Create empty embbedings
    empty_embeddings = np.array([])  
    ids = []  
    with open('tests/data/empty_embeddings.pkl', 'wb') as f:
        pickle.dump({'embeddings': empty_embeddings, 'ids': ids}, f)

    # Use the empty embbedings
    vectorizer = Vectorizer(sample_recipes, embeddings_file='tests/data/empty_embeddings.pkl')

    assert vectorizer.embeddings is not None and vectorizer.embeddings.size > 0, "Embbedings should be created."
    assert vectorizer.index is not None, "Faiss should exists"

# Test for the case where the embeddings file doesn't exist
def test_embeddings_file_not_found_and_generating(sample_recipes):
    # Ensure that the embeddings file does not exist
    embeddings_file = 'non_existent_embeddings.pkl'
    if os.path.exists(embeddings_file):
        os.remove(embeddings_file)  # Remove if it already exists

    # Create the Vectorizer, which should try to regenerate the embeddings
    vectorizer = Vectorizer(sample_recipes, embeddings_file=embeddings_file)

    # Check that embeddings have been created
    assert vectorizer.embeddings is not None and vectorizer.embeddings.size > 0, "Embeddings should have been created."

    # Check that the FAISS index has been generated
    assert vectorizer.index is not None, "FAISS index should have been generated."

    # Verify that the embeddings file has been created (it should have been regenerated)
    assert os.path.exists(embeddings_file), "Embeddings file should have been created."

# Test for when embeddings are empty or not in the correct format
def test_embeddings_invalid_format(sample_recipes):
    # Create invalid embeddings (not a 2D array)
    invalid_embeddings = np.array([1])  # 1D array instead of 2D
    ids = [1]
    
    # Save invalid embeddings to a file
    with open('invalid_embeddings.pkl', 'wb') as f:
        pickle.dump({'embeddings': invalid_embeddings, 'ids': ids}, f)

    # Create a Vectorizer instance with invalid embeddings
    vectorizer = Vectorizer(sample_recipes, embeddings_file='invalid_embeddings.pkl')
