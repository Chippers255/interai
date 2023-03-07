from abc import ABC, abstractmethod
from typing import List


class Splitter(ABC):
    """The base class for all document splitters."""

    @abstractmethod
    def split_document(self, document: str) -> List[str]:
        """Take a document and split it into pages."""


def validate_document(document: str) -> None:
    """Perform a series of checks to confirm if the document is valid for use."""
    if type(document) != str:
        raise TypeError("the document must be a string type")
    if document == "":
        raise ValueError("document is empty")
