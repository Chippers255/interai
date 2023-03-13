import unittest

from interai.splitter.splitter import validate_document


class TestValidateDocument(unittest.TestCase):
    def test_for_success(self):
        test_doc = "this is some text"
        resp = validate_document(test_doc)
        self.assertIsNone(resp)

    def test_for_type_error(self):
        with self.assertRaises(TypeError) as context:
            _ = validate_document(1)
        self.assertTrue("the document must be a string type" in str(context.exception))

    def test_for_value_error(self):
        with self.assertRaises(ValueError) as context:
            _ = validate_document("")
        self.assertTrue("document is empty" in str(context.exception))
