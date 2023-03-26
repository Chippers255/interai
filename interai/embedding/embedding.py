from abc import ABC, abstractmethod
from typing import List


class Embedding(ABC):
    """The base class for all document and document collection embedding."""

    @abstractmethod
    def document_embedding(self, document: str) -> List[float]:
        """Take a document and create a vector representation."""

    @abstractmethod
    def collection_embedding(self, collection: List[str]) -> List[List[float]]:
        """Take a collection of documents and create vector representations for each."""
