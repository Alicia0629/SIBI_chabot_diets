import pickle
import pandas as pd
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

def load_recipes(file_path):
    total_rows = sum(1 for _ in open(file_path)) - 1
    chunk_size = total_rows // 50 + 1  

    chunks = []
    with tqdm(total=total_rows, desc="Loading CSV") as pbar:
        for chunk in pd.read_csv(file_path, chunksize=chunk_size):
            chunks.append(chunk)
            pbar.update(len(chunk))  

    return pd.concat(chunks, ignore_index=True)

def generate_embeddings(df):
    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')  
    text_data = df['Name'] + " " + df['Description'].fillna('')  
    embeddings = model.encode(text_data.tolist(), show_progress_bar=True)  
    recipe_ids = df['RecipeId'].tolist()  
    return embeddings, recipe_ids

def save_embeddings_to_pickle(embeddings, recipe_ids, filename='../datasets/embeddings.pkl'):
    with open(filename, 'wb') as f:
        pickle.dump({'embeddings': embeddings, 'ids': recipe_ids}, f)
    print(f"Embeddings and Recipe IDs saved in {filename}")

def main():
    file_path = '../datasets/NewRecipes.csv'  
    df = load_recipes(file_path)  
    embeddings, recipe_ids = generate_embeddings(df) 
    save_embeddings_to_pickle(embeddings, recipe_ids) 

if __name__ == "__main__":
    main()
