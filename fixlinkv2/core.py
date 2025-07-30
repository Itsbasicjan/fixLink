"""fixlinkv2 – entfernt leere 'link'‑Felder aus allen API‑Aufrufen."""

from django.utils.translation import gettext_lazy as _

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

    def ready(self):
        """
        Wird von InvenTree nach dem App‑Bootstrap aufgerufen.
        Der Import oben reicht schon – ready() nur damit klar ist,
        dass das Plugin Signal‑Handler nutzt.
        """
        super().ready()