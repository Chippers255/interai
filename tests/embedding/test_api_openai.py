import unittest
from unittest.mock import patch

from interai.embedding.api_openai import OpenAIEmbedding


class TestOpenAIEmbedding(unittest.TestCase):
    def setUp(self):
        self.embedding = OpenAIEmbedding()

    def test_document_embedding(self):
        with patch("openai.Embedding.create") as mock_create:
            mock_create.return_value = {"data": [{"embedding": [0.1, 0.2]}]}
            document = "Test document 123."
            expected_embedding = [0.1, 0.2]

            result = self.embedding.document_embedding(document)
            self.assertEqual(result, expected_embedding)

    def test_document_embedding_invalid_document(self):
        with self.assertRaises(ValueError):
            self.embedding.document_embedding("")

    def test_collection_embedding(self):
        with patch("openai.Embedding.create") as mock_create:
            mock_create.return_value = {"data": [{"embedding": [0.1, 0.2]}, {"embedding": [0.3, 0.4]}]}
            collection = ["Test document 1.", "Test document 2."]
            expected_embedding = [
                [0.1, 0.2],
                [0.3, 0.4],
            ]

            result = self.embedding.collection_embedding(collection)
            self.assertEqual(result, expected_embedding)

    def test_collection_embedding_invalid_document(self):
        with self.assertRaises(ValueError):
            self.embedding.collection_embedding(["Test document 1.", ""])


if __name__ == "__main__":
    unittest.main()
