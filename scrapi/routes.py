#!/usr/bin/env python3

from flask import jsonify
from scrapi import app, html

full_names, shortcuts = [], []


@app.route("/engines/all", methods=["GET"])
def engines_all():
    for name in html.find_all("th", {"class": None}):
        full_names.append(name.get_text())

    to_remove = [
        "Allow",
        "Engine name",
        "Shortcut",
        "Selected language",
        "SafeSearch",
        "Time range",
        "Avg. time",
        "Max time",
    ]
    while any(item in to_remove for item in full_names):
        for text in to_remove:
            full_names.remove(text)
    for shortcut in html.find_all("td", {"class": "name"}):
        shortcuts.append(shortcut.get_text())

    engines = []
    for i in range(len(full_names)):
        engines.append(
            {
                "name": full_names[i],
                "shortcut": shortcuts[i]
            }
        )

    return jsonify(engines)
