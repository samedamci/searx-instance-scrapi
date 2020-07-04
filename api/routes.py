#!/usr/bin/env python3

from flask import jsonify, request
from api import app
from scrapper import Engines, General
from scrapper.request import get_html


@app.route("/general/default", methods=["GET"])
def general_default():
    defaults = General(get_html()).default()

    return jsonify(defaults)


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
