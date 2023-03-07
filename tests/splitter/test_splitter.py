import unittest
from typing import List

from interai.splitter.splitter import Splitter


class GoodTestSplitter(Splitter):
    def __init__(self):
        self.pointless = "pointless"

    def split_document(self, document: str) -> List[str]:
        return document.split(" ")


class BadTestSplitter(Splitter):
    def __init__(self):
        self.pointless = "pointless"

    def pprint(self):
        print(self.pointless)


class TestBaseSplitter(unittest.TestCase):
    def test_for_success(self):
        test_instance = GoodTestSplitter()
        self.assertIsInstance(test_instance, Splitter)
        self.assertEqual(test_instance.split_document("this is some text"), ["this", "is", "some", "text"])

    def test_for_failure_with_missing_split_document(self):
        with self.assertRaises(TypeError) as context:
            _ = BadTestSplitter()
        self.assertTrue("Can't instantiate abstract class BadTestSplitter with abstract method split_document" in str(context.exception))


if __name__ == "__main__":
    unittest.main()
