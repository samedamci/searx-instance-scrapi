#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests

INSTANCE_URL = "https://searx.samedamci.me"

html_doc = requests.get(f"{INSTANCE_URL}/preferences").content
html = BeautifulSoup(html_doc, "html.parser")
