from typing import List

import requests
import validators
from bs4 import BeautifulSoup

from interai.reader.reader import Reader
from interai.splitter.character_splitter import CharacterSplitter
from interai.splitter.splitter import Splitter


class URLReader(Reader):
    def __init__(self, url: str):
        if not validators.url(url):
            raise ValueError("not a valid url to read text from")
        self.url = url

    def read(self) -> str:
        page = requests.get(self.url)
        if page.status_code != 200:
            raise ValueError(f"unable to scrape url {self.url}, received http status {page.status_code}")
        soup = BeautifulSoup(page.content, "html.parser")
        text = soup.get_text()
        text = text.strip()
        return text

    def read_and_split(self, splitter: Splitter = None) -> List[str]:
        document = self.read()
        if splitter is None:
            splitter = CharacterSplitter()
        return splitter.split_document(document)
