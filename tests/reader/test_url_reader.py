import unittest

import responses

from interai.reader.url_reader import URLReader
from interai.splitter.character_splitter import CharacterSplitter

FAKE_ARTICLE = """<html>
<head><title>A Fake Article</title></head>
<body><p>This is the text from a fake article.</p></body>
</html>"""
FAKE_ARTICLE_TEXT = "A Fake Article\nThis is the text from a fake article."
SPLIT_FAKE_ARTICLE_TEXT = ["A Fake Art", "rticle\nThi", "his is the", "he text fr", "from a fak", "ake articl", "cle."]


class TestURLReader(unittest.TestCase):
    def test_init_for_success(self):
        url = "https://www.somefakesite.ca"
        test_instance = URLReader(url)
        self.assertIsInstance(test_instance, URLReader)
        self.assertEqual(test_instance.url, url)

    def test_init_for_value_error_with_bad_url(self):
        url = "not a url"
        with self.assertRaises(ValueError) as context:
            _ = URLReader(url)
        self.assertTrue("not a valid url to read text from" in str(context.exception))

    def test_read_for_success(self):
        url = "https://www.somefakesite.ca"
        with responses.RequestsMock() as rsps:
            rsps.add(responses.GET, url, body=FAKE_ARTICLE, status=200)
            test_instance = URLReader(url)
            text = test_instance.read()
            self.assertEqual(text, FAKE_ARTICLE_TEXT)

    def test_read_for_value_error_with_bad_status(self):
        url = "https://www.somefakesite.ca"
        with self.assertRaises(ValueError) as context:
            with responses.RequestsMock() as rsps:
                rsps.add(responses.GET, url, body=FAKE_ARTICLE, status=404)
                test_instance = URLReader(url)
                _ = test_instance.read()
        self.assertTrue(f"unable to scrape url {url}, received http status 404" in str(context.exception))

    def test_read_and_split_for_success_with_default_splitter(self):
        url = "https://www.somefakesite.ca"
        with responses.RequestsMock() as rsps:
            rsps.add(responses.GET, url, body=FAKE_ARTICLE, status=200)
            test_instance = URLReader(url)
            split_text = test_instance.read_and_split()
            self.assertEqual(split_text, [FAKE_ARTICLE_TEXT])

    def test_read_and_split_for_success_with_custom_splitter(self):
        url = "https://www.somefakesite.ca"
        splitter = CharacterSplitter(page_length=10, overlap_length=2)
        with responses.RequestsMock() as rsps:
            rsps.add(responses.GET, url, body=FAKE_ARTICLE, status=200)
            test_instance = URLReader(url)
            split_text = test_instance.read_and_split(splitter)
            self.assertEqual(split_text, SPLIT_FAKE_ARTICLE_TEXT)


if __name__ == "__main__":
    unittest.main()
