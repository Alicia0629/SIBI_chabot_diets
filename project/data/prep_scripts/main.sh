mkdir ../datasets
python3 createDatasetAllergies.py
python3 dowloadFoodDataset.py

python3 newFoodDataset.py

python3 createTestRecipes.py

python3 createEmbbedingsPickle.py