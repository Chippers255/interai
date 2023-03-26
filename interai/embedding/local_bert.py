import re
from typing import List

from sentence_transformers import SentenceTransformer

from interai.embedding.embedding import Embedding
from interai.splitter.splitter import validate_document


class LocalBERTEmbedding(Embedding):
    def __init__(self, model="sentence-t5-base"):
        self.model = model
        self.model_instance = SentenceTransformer(model)

    def document_embedding(self, document: str) -> List[float]:
        validate_document(document)
        doc_fix = re.sub("[^A-Za-z0-9 ]+", "", document)
        doc_fix = doc_fix.lower()
        embedding = self.model_instance.encode(doc_fix)
        return embedding

    def collection_embedding(self, collection: List[str]) -> List[List[float]]:
        resp_list = []
        for document in collection:
            resp_list.append(self.document_embedding(document))
        return resp_list
