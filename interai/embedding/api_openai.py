import re
from typing import List

import openai

from interai.embedding.embedding import Embedding
from interai.splitter.splitter import validate_document


class OpenAIEmbedding(Embedding):
    def __init__(self, model="text-embedding-ada-002"):
        self.model = model

    def document_embedding(self, document: str) -> List[float]:
        validate_document(document)
        doc_fix = re.sub("[^A-Za-z0-9 ]+", "", document)
        doc_fix = doc_fix.lower()
        response = openai.Embedding.create(input=doc_fix, model=self.model)
        embedding = response["data"][0]["embedding"]
        return embedding

    def collection_embedding(self, collection: List[str]) -> List[List[float]]:
        doc_list_fix = []
        for document in collection:
            validate_document(document)
            doc_fix = re.sub("[^A-Za-z0-9 ]+", "", document)
            doc_fix = doc_fix.lower()
            doc_list_fix.append(doc_fix)
        response = openai.Embedding.create(input=doc_list_fix, model=self.model)
        embedding = [x["embedding"] for x in response["data"]]
        return embedding
