"""fixlinkv2 – entfernt leere 'link'‑Felder aus allen API‑Aufrufen."""

from django.utils.translation import gettext_lazy as _
from django.urls import resolve            # hilft beim Routen‑Match

from plugin import InvenTreePlugin
from plugin.mixins import (
    SettingsMixin,
    ValidationMixin,
    UserInterfaceMixin,   # <‑‑ neu
)
from . import signals

from . import PLUGIN_VERSION

class fixlinkv2(UserInterfaceMixin, SettingsMixin, ValidationMixin, InvenTreePlugin):
    """Custom‑Plugin, das einen globalen JS‑Patch in die UI einbindet."""

    NAME = SLUG = TITLE = "fixlinkv2"
    DESCRIPTION = _("Entfernt leere 'link'‑Felder aus API‑Requests")
    VERSION = PLUGIN_VERSION
    AUTHOR = "Jan Schüler"
    LICENSE = "MIT"

    def get_ui_page_scripts(self, request, context, **kwargs):
        """
        Wird bei jedem Seitenaufruf gefragt, welche Skripte
        für die aktuelle URL injiziert werden sollen.
        """
        match = resolve(request.path_info)

        # Prüfen, ob wir auf der Teile‑Listen‑Seite sind
        if match.url_name == 'part-index':     # <‑ passt für 0.12+; älter: 'part-list'
            return [{
                "key": "fixlinkv2-parts-patch",
                "source": self.plugin_static_file("fixlink_patch.js:initPatch"),
            }]

        # alle anderen Seiten: nichts einbinden
        return []