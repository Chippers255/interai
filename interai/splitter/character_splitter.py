from typing import List

from interai.splitter.splitter import Splitter, validate_document


class CharacterSplitter(Splitter):
    """A document splitter that splits documents into pages based on character lgnths."""

    def __init__(self, page_length: int = 1000, overlap_length: int = 200):
        if page_length < overlap_length:
            raise ValueError("overlap length cannot be larger than page length")
        self.page_length = page_length
        self.overlap_length = overlap_length

    def split_document(self, document: str) -> List[str]:
        """Take a document and split it into pages based on character lengths."""
        validate_document(document)
        pages = []
        document_length = len(document)
        start_index = 0
        while start_index < document_length:
            end_index = min(start_index + self.page_length, document_length)
            pages.append(document[start_index:end_index])
            start_index += self.page_length - self.overlap_length
        return pages
