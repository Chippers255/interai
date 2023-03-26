import unittest

import numpy

from interai.embedding.local_bert import LocalBERTEmbedding


class TestLocalBERTEmbedding(unittest.TestCase):
    def setUp(self):
        self.embedding = LocalBERTEmbedding()

    def test_default_create(self):
        test_instance = LocalBERTEmbedding()
        self.assertIsInstance(test_instance, LocalBERTEmbedding)
        self.assertEqual(test_instance.model, "sentence-t5-base")

    def test_custom_create(self):
        test_instance = LocalBERTEmbedding(model="paraphrase-MiniLM-L6-v2")
        self.assertIsInstance(test_instance, LocalBERTEmbedding)
        self.assertEqual(test_instance.model, "paraphrase-MiniLM-L6-v2")

    def test_document_embedding(self):
        # Test with a valid document
        valid_document = "This is a sample document."
        embedding = self.embedding.document_embedding(valid_document)
        self.assertIsInstance(embedding, numpy.ndarray)

        # Test with an invalid document
        invalid_document = ""
        self.assertRaises(ValueError, self.embedding.document_embedding, invalid_document)

    def test_collection_embedding(self):
        # Test empty collection
        empty_collection = []
        self.assertEqual(self.embedding.collection_embedding(empty_collection), [])

        # Test valid non-empty collection
        valid_collection = ["Document 1", "Document 2"]
        embeddings = self.embedding.collection_embedding(valid_collection)
        self.assertIsInstance(embeddings, list)
        self.assertEqual(len(embeddings), 2)
        self.assertIsInstance(embeddings[0], numpy.ndarray)

        # Test invalid collection with empty document
        invalid_collection = ["Document 1", ""]
        self.assertRaises(ValueError, self.embedding.collection_embedding, invalid_collection)


if __name__ == "__main__":
    unittest.main()
