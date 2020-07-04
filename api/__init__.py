#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)
from api import routes
