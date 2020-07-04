#!/usr/bin/env python3

from flask import jsonify
from api import app, engines


@app.route("/engines/all", methods=["GET"])
def engines_all():
    return jsonify(engines.all())
