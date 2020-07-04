#!/usr/bin/env python3

from flask import Flask
from scrapper.engines import Engines

app = Flask(__name__)
engines = Engines()

from api import routes
