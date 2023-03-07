import unittest
from typing import List

from interai.reader.reader import Reader


class GoodTestReader(Reader):
    def __init__(self):
        self.text = "this is some text"

    def read(self) -> str:
        return self.text

    def read_and_split(self) -> List[str]:
        return self.text.split(" ")


class BadTestReader1(Reader):
    def __init__(self):
        self.text = "this is some text"

    def read(self) -> str:
        return self.text


class BadTestReader2(Reader):
    def __init__(self):
        self.text = "this is some text"

    def read_and_split(self) -> List[str]:
        return self.text.split(" ")


class TestBaseReader(unittest.TestCase):
    def test_for_success(self):
        test_instance = GoodTestReader()
        self.assertIsInstance(test_instance, Reader)
        self.assertEqual(test_instance.read(), "this is some text")
        self.assertEqual(test_instance.read_and_split(), ["this", "is", "some", "text"])

    def test_for_failure_with_missing_read_and_split(self):
        with self.assertRaises(TypeError) as context:
            _ = BadTestReader1()
        self.assertTrue("Can't instantiate abstract class BadTestReader1 with abstract method read_and_split" in str(context.exception))

    def test_for_failure_with_missing_read(self):
        with self.assertRaises(TypeError) as context:
            _ = BadTestReader2()
        self.assertTrue("Can't instantiate abstract class BadTestReader2 with abstract method read" in str(context.exception))


if __name__ == "__main__":
    unittest.main()
