import faiss
import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np
import os
from tqdm import tqdm

class Vectorizer:
    def __init__(self, recipes_df, index_file='recipes.index'):
        """
        Inicia el vectorizador con un DataFrame de recetas y carga o genera el índice FAISS.
        :param recipes_df: DataFrame con recetas.
        :param index_file: Archivo donde se guardará el índice FAISS.
        """
        self.recipes_df = recipes_df
        self.model = SentenceTransformer('paraphrase-MiniLM-L6-v2') 
        self.index_file = index_file
        self.index = None
        
        if os.path.exists(self.index_file):
            print(f"Cargando índice desde {self.index_file}")
            self.index = faiss.read_index(self.index_file)
        else:
            print("Generando índice FAISS")
            self.build_index()

    def build_index(self):
        """
        Construye el índice FAISS usando los embeddings de todas las recetas.
        """
        print(0)
        text_data = (
            self.recipes_df['Name'] + " " + self.recipes_df['Description'].fillna("")
        ).tolist()

        print(1)
        with tqdm(total=len(text_data), desc="Generando embeddings y construyendo índice") as pbar:
            # Generar los embeddings para cada receta y agregar al índice
            embeddings = []
            for i in range(len(text_data)):
                embedding = self.model.encode([text_data[i]], convert_to_numpy=True)
                embeddings.append(embedding)
                pbar.update(1)  # Actualizar la barra de progreso

            embeddings = np.vstack(embeddings)  # Convertir la lista de embeddings en un array NumPy

        
        print(2)
        self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(embeddings)

        print(3)
        faiss.write_index(self.index, self.index_file)
        print(f"Índice guardado en {self.index_file}")

    def search(self, query, k=5, filters=None):
        """
        Buscar en el índice usando un query y devolver las recetas más relevantes.
        :param query: Consulta de búsqueda.
        :param k: Número de resultados a devolver.
        :param filters: Filtros de restricciones dietéticas a aplicar antes de la búsqueda.
        :return: DataFrame con las recetas relevantes.
        """
        if filters:
            filtered_recipes = self.filter_recipes(filters)
        else:
            filtered_recipes = self.recipes_df

        # Generar embeddings de la consulta
        query_embedding = self.model.encode([query], convert_to_numpy=True)

        # Buscar en el índice
        distances, indices = self.index.search(query_embedding, k)

        # Devolver las recetas relevantes (después de aplicar los filtros)
        return filtered_recipes.iloc[indices[0]]

    def filter_recipes(self, filters):
        """
        Filtra las recetas según las restricciones dietéticas proporcionadas.
        :param filters: Diccionario con restricciones dietéticas (por ejemplo, alergias).
        :return: DataFrame filtrado.
        """
        filtered = self.recipes_df
        for key, value in filters.items():
            if key in filtered.columns:
                filtered = filtered[filtered[key] == value]
        return filtered
