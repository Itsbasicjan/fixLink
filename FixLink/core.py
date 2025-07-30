"""FixLink - Entfernt leere 'link'-Felder bei neuen oder bearbeiteten Teilen."""

from plugin import InvenTreePlugin
from plugin.mixins import PartMixin  # Wichtig!
from part.models import Part


class FixLink(PartMixin, InvenTreePlugin):
    NAME = "FixLink"
    SLUG = "fixlink"
    TITLE = "FixLink"
    VERSION = "1.0"
    DESCRIPTION = "Plugin entfernt leere Strings im Feld 'link', um API-Fehler zu verhindern."

    AUTHOR = "Jan Schüler"
    WEBSITE = "https://inventur.asta-hsh.de"
    LICENSE = "MIT"

    def pre_save_part(self, sender, instance: Part, data: dict, user, **kwargs):
        """Entfernt 'link' aus den Daten, wenn es leer ist"""
        if isinstance(data, dict) and data.get("link", "").strip() == "":
            data.pop("link", None)
