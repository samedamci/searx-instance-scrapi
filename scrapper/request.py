#!/usr/bin/env python3

from scrapper import INSTANCE_URL
from bs4 import BeautifulSoup
import requests


def get_html() -> BeautifulSoup:
    """Function makes GET request to instance and downloads raw HTML code
    which is parsing after."""
    html_doc = requests.get(f"{INSTANCE_URL}/preferences").content
    html = BeautifulSoup(html_doc, "html.parser")

    return html
