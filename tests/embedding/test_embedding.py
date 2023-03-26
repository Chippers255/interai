import unittest
from typing import List

from interai.embedding.embedding import Embedding


class GoodTestEmbedding(Embedding):
    def __init__(self):
        self.text = "this is some text"

    def document_embedding(self, document: str) -> List[float]:
        print(document)
        return [0.1239, -0.9234, 0.3345]

    def collection_embedding(self, collection: List[str]) -> List[List[float]]:
        vectors = [[0.1239, -0.9234, 0.3345] for i in range(len(collection))]
        return vectors


class BadTestEmbedding1(Embedding):
    def __init__(self):
        self.text = "this is some text"

    def document_embedding(self, document: str) -> List[float]:
        print(document)
        return [0.1239, -0.9234, 0.3345]


class BadTestEmbedding2(Embedding):
    def __init__(self):
        self.text = "this is some text"

    def collection_embedding(self, collection: List[str]) -> List[List[float]]:
        vectors = [[0.1239, -0.9234, 0.3345] for i in range(len(collection))]
        return vectors


class TestBaseEmbedding(unittest.TestCase):
    def test_for_success(self):
        test_instance = GoodTestEmbedding()
        self.assertIsInstance(test_instance, Embedding)
        self.assertEqual(test_instance.document_embedding("this is some text"), [0.1239, -0.9234, 0.3345])
        self.assertEqual(test_instance.collection_embedding(["this", "is"]), [[0.1239, -0.9234, 0.3345], [0.1239, -0.9234, 0.3345]])

    def test_for_failure_with_missing_collection_embedding(self):
        with self.assertRaises(TypeError) as context:
            _ = BadTestEmbedding1()
        self.assertTrue("Can't instantiate abstract class BadTestEmbedding1 with abstract method collection_embedding" in str(context.exception))

    def test_for_failure_with_missing_document_embedding(self):
        with self.assertRaises(TypeError) as context:
            _ = BadTestEmbedding2()
        self.assertTrue("Can't instantiate abstract class BadTestEmbedding2 with abstract method document_embedding" in str(context.exception))


if __name__ == "__main__":
    unittest.main()
