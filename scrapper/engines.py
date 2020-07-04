#!/usr/bin/env python3

from scrapper import html


class Engines:
    def __init__(self):
        self.full_names, self.shortcuts = [], []
        for name in html.find_all("th", {"class": None}):
            self.full_names.append(name.get_text())

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
        while any(item in to_remove for item in self.full_names):
            for text in to_remove:
                self.full_names.remove(text)
        for shortcut in html.find_all("td", {"class": "name"}):
            self.shortcuts.append(shortcut.get_text())

    def all(self):
        self.all_engines = []
        for i in range(len(self.full_names)):
            self.all_engines.append(
                {"name": self.full_names[i], "shortcut": self.shortcuts[i]}
            )

        return self.all_engines
