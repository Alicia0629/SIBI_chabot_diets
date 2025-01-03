import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from tqdm import tqdm
import os

class Vectorizer:
    def __init__(self, recipes_df, index_file='data/datasets/recipes.index', embeddings_file='data/datasets/embeddings.pkl'):
        """
        Initialize vectorizer with a DataFrame of recipes and load or generate FAISS index.
        :param recipes_df: DataFrame with recipes.
        :param index_file: File where the FAISS index will be saved.
        :param embeddings_file: File where the embeddings are stored.
        """
        self.recipes_df = recipes_df
        self.model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
        self.index_file = index_file
        self.embeddings_file = embeddings_file
        self.index = None
        self.embeddings = None

        if os.path.exists(self.embeddings_file):
            print(f"Loading embeddings from {self.embeddings_file}")
            with open(self.embeddings_file, 'rb') as f:
                data = pickle.load(f)
                embeddings_pickle = data['embeddings']
                ids_pickle = data['ids']

                # Optimized filtering
                valid_ids_set = set(self.recipes_df['RecipeId'].tolist())
                filtered_indices = [
                    i for i, id_ in tqdm(enumerate(ids_pickle), total=len(ids_pickle), desc="Filtering indices")
                    if id_ in valid_ids_set
                ]

                self.embeddings = np.array(
                    [embeddings_pickle[i] for i in tqdm(filtered_indices, desc="Building embeddings")]
                )

            if self.embeddings.size == 0:
                print("No embeddings matched the dataset. Regenerating embeddings.")
                self.build_index()
            else:
                print(f"Embeddings loaded, shape: {self.embeddings.shape}")
                self.build_index()
        else:
            print("Embeddings file not found, generating embeddings.")
            self.build_index()

    def build_index(self):
        """
        Build the FAISS index using embeddings from all recipes.
        """
        print("Generating FAISS index...")

        if self.embeddings is None or self.embeddings.size == 0:
            text_data = (
                self.recipes_df['Name'] + " " + self.recipes_df['Description'].fillna("")
            ).tolist()

            print("Generating embeddings and building index...")
            self.embeddings = self.model.encode(text_data, convert_to_numpy=True, show_progress_bar=True)

            # Save embeddings along with IDs
            ids = self.recipes_df['RecipeId'].tolist()
            with open(self.embeddings_file, 'wb') as f:
                pickle.dump({'embeddings': self.embeddings, 'ids': ids}, f)
                print(f"Embeddings saved to {self.embeddings_file}")

        # Build FAISS index
        if self.embeddings is not None and self.embeddings.ndim == 2:
            self.index = faiss.IndexFlatL2(self.embeddings.shape[1])  # Use shape[1] for dimensions
            self.index.add(self.embeddings)

            # Optionally, save the FAISS index
            faiss.write_index(self.index, self.index_file)
            print(f"FAISS index built and saved to {self.index_file}")

    def search(self, query, k=5):
        """
        Search in the index using a query and return the most relevant recipes.
        :param query: Search query.
        :param k: Number of results to return.
        :return: DataFrame with relevant recipes.
        """
        if self.index is None:
            raise Exception("FAISS index has not been initialized.")
        
        query_embedding = self.model.encode([query], convert_to_numpy=True)

        distances, indices = self.index.search(query_embedding, k)
        return self.recipes_df.iloc[indices[0]]
