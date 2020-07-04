#!/usr/bin/env python3

from flask import jsonify
from api import app
from scrapper.engines import Engines
from scrapper.request import get_html


@app.route("/engines/all", methods=["GET"])
def engines_all():
    engines = Engines(get_html())

    return jsonify(engines.all())
