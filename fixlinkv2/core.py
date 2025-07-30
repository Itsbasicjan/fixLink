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
    """fixlinkv2 – custom InvenTree plugin."""

    # Basis‑Metadaten
    NAME = SLUG = TITLE = "fixlinkv2"
    DESCRIPTION = _("Entfernt leere 'link'‑Felder aus API‑Requests")
    VERSION = PLUGIN_VERSION
    AUTHOR = "Jan Schüler"
    LICENSE = "MIT"

    # -------------------------------------------------------------
    #  UI‑Mixin: winziges (unsichtbares) Dashboard‑Item, das nur
    #  unsere JS‑Datei lädt und sofort wieder verschwindet
    # -------------------------------------------------------------
    def get_ui_dashboard_items(self, request, context, **kwargs):
        """Registriert ein unsichtbares Loader‑Item, das fixlink_patch.js ausführt."""
        return [
            {
                "key": "fixlinkv2-loader",
                "title": "",              # leer ⇒ keine Box‑Überschrift
                "description": "",
                "icon": "",               # kein Icon
                # JS‑Datei + Funktionsname hinter dem ':'
                "source": self.plugin_static_file("fixlink_patch.js:initPatch"),
                # minimales 2×2‑Raster – kleiner geht aktuell nicht
                "options": {"width": 2, "height": 2},
            }
        ]
