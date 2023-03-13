import unittest

from interai.splitter.character_splitter import CharacterSplitter

FAKE_ARTICLE_TEXT = "A Fake Article\nThis is the text from a fake article."
SPLIT_FAKE_ARTICLE_TEXT = ["A Fake Art", "rticle\nThi", "his is the", "he text fr", "from a fak", "ake articl", "cle."]


class TestCharacterSplitter(unittest.TestCase):
    def test_for_success_with_defaults(self):
        test_instance = CharacterSplitter()
        self.assertIsInstance(test_instance, CharacterSplitter)
        self.assertEqual(test_instance.page_length, 1000)
        self.assertEqual(test_instance.overlap_length, 200)
        self.assertEqual(test_instance.split_document("this is some text"), ["this is some text"])

    def test_for_success_with_custom_limits(self):
        test_instance = CharacterSplitter(page_length=10, overlap_length=2)
        self.assertIsInstance(test_instance, CharacterSplitter)
        self.assertEqual(test_instance.page_length, 10)
        self.assertEqual(test_instance.overlap_length, 2)
        self.assertEqual(test_instance.split_document(FAKE_ARTICLE_TEXT), SPLIT_FAKE_ARTICLE_TEXT)

    def test_for_failure_with_bad_limits(self):
        with self.assertRaises(ValueError) as context:
            _ = CharacterSplitter(page_length=1, overlap_length=2)
        self.assertTrue("overlap length cannot be larger than page length" in str(context.exception))
