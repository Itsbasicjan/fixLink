"""fixlinkv2 – entfernt leere 'link'‑Felder aus allen API‑Aufrufen."""

from django.utils.translation import gettext_lazy as _

from plugin import InvenTreePlugin
from plugin.mixins import (
    SettingsMixin,
    ValidationMixin,
    UserInterfaceMixin,   # <‑‑ neu
)

from . import PLUGIN_VERSION

class fixlinkv2(UserInterfaceMixin, SettingsMixin, ValidationMixin, InvenTreePlugin):
    """Custom‑Plugin, das einen globalen JS‑Patch in die UI einbindet."""

    NAME = SLUG = TITLE = "fixlinkv2"
    DESCRIPTION = _("Entfernt leere 'link'‑Felder aus API‑Requests")
    VERSION = PLUGIN_VERSION
    AUTHOR = "Jan Schüler"
    LICENSE = "MIT"

    # ------------------------------------------------------------------
    #  UI‑Hook: globales Skript, wird unmittelbar nach dem UI‑Bootstrap
    #  geladen – dadurch ist der Patch auf allen Seiten sofort aktiv.
    # ------------------------------------------------------------------
    def get_ui_global_scripts(self, request, context, **kwargs):
        """Liefert die JS‑Datei, die den XMLHttpRequest/fetch‑Patch enthält."""
        return [
            {
                "key": "fixlinkv2-global-patch",
                "source": self.plugin_static_file("fixlink_patch.js:initPatch"),
            }
        ]