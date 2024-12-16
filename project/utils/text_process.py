from sklearn.metrics.pairwise import cosine_similarity
import cohere
import re
from config import KEY_SIMILARITY


co = cohere.ClientV2(KEY_SIMILARITY)


def text_similarity(phrase:str,texts:list)->str:
    newTexts = texts.copy()
    newTexts.append(phrase)
    response = co.embed(
        texts=newTexts,
        model='embed-multilingual-v3.0',
        input_type='search_document',
        embedding_types=['float']
    )
    embeddings = response.embeddings.float
    print(newTexts)
    print(texts)

    similarities = cosine_similarity(embeddings[:-1], [embeddings[-1]]).flatten()

    max_index = similarities.argmax()

    print(similarities)
    print(max_index)
    print(texts[max_index])

    return texts[max_index]

def extract_numbers(value):
    match = re.search(r'\d+(?:\.\d+)?', value)
    return float(match.group()) if match else None

