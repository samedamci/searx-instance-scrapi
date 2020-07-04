#!/usr/bin/env python3

from flask import jsonify, request
from api import app
from scrapper.engines import Engines
from scrapper.request import get_html


@app.route("/engines", methods=["GET"])
def engines():
    if "name" in request.args:
        query = str(request.args["name"])
        engine = Engines(get_html()).get_by_name(query)

        return jsonify(engine)


@app.route("/engines/all", methods=["GET"])
def engines_all():
    engines = Engines(get_html()).all()

    return jsonify(engines)
