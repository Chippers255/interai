from abc import ABC, abstractmethod
from typing import List


class Reader(ABC):
    """The base class for all document readers."""

    @abstractmethod
    def read(self) -> str:
        """Read from a document source and return the text as a single string."""

    @abstractmethod
    def read_and_split(self) -> List[str]:
        """Read from a document source and return the text split into pages."""
