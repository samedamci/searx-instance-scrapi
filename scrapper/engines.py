#!/usr/bin/env python3

class Engines:
    """Get informations about engines preferences."""
    def __init__(self, html):
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
        """Get all engines and shortcuts."""
        self.all_engines = []
        for i in range(len(self.full_names)):
            self.all_engines.append(
                {"name": self.full_names[i], "shortcut": self.shortcuts[i]}
            )

        return self.all_engines

    def get_by_name(self, query_name):
        """Get infromations about engine by name."""
        all_engines = self.all()
        for i in range(len(all_engines)):
            engine_name = all_engines[i]['name']
            if query_name == engine_name:
                shortcut = all_engines[i]['shortcut']
                return {"shortcut": shortcut}
