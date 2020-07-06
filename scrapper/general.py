#!/usr/bin/env python3


class General:
    """Get general settings."""
    def __init__(self, html: str):
        self.selected = []
        for selection in html.find_all("option", {"selected": "selected"}):
            self.selected.append(selection.get_text())

    def default(self) -> dict:
        """Get general settings default values."""
        if self.selected[3] == "Enabled":
            self.selected[3] = True
        else:
            self.selected[3] = False

        if self.selected[5] == "None":
            self.selected[5] = None

        if self.selected[8] == "On":
            self.selected[8] = True
        else:
            self.selected[8] = False

        default_values = {
            "search_language": self.selected[0],
            "interface_language": self.selected[1],
            "autocomplete": self.selected[2],
            "image_proxy": self.selected[3],
            "method": self.selected[4],
            "safe_search": self.selected[5],
            "theme": self.selected[6],
            "style": self.selected[7],
            "results_on_new_tabs": self.selected[8],
        }

        return default_values
