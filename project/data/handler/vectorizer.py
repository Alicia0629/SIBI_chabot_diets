from sentence_transformers import SentenceTransformer
import faiss

class Vectorizer:
    def __init__(self, recipes_df):
        """
        Start vectorizer with DataFrame of recipes.
        :param recipes_df: DataFrame with recipes.
        """
        self.recipes_df = recipes_df
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = None
        self._build_index()

    def build_index(self):
        """
        Build an FAISS index using embeddings
        """
        text_data = (
            self.recipes_df['Name'] + " " + self.recipes_df['Description'].fillna("")
        ).tolist()
        embeddings = self.model.encode(text_data)
        self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(embeddings)

    def search(self, query, k=5):
        """
        Search in the index.
        :param query: Search question
        :param k: Number of result to return
        :return: DataFrame with revelant recipes
        """
        query_embedding = self.model.encode([query])
        distances, indices = self.index.search(query_embedding, k)
        return self.recipes_df.iloc[indices[0]]

