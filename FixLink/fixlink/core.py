"""A short description of the project"""

from plugin import InvenTreePlugin

from plugin.mixins import SettingsMixin

from . import PLUGIN_VERSION


class FixLink(SettingsMixin, InvenTreePlugin):

    """FixLink - custom InvenTree plugin."""

    # Plugin metadata
    TITLE = "FixLink"
    NAME = "FixLink"
    SLUG = "fixlink"
    DESCRIPTION = "A short description of the project"
    VERSION = PLUGIN_VERSION

    # Additional project information
    AUTHOR = "Jan Schüler"
    WEBSITE = "https://inventur.asta-hsh.de"
    LICENSE = "MIT"

    # Optionally specify supported InvenTree versions
    # MIN_VERSION = '0.18.0'
    # MAX_VERSION = '2.0.0'
    
    
    # Plugin settings (from SettingsMixin)
    # Ref: https://docs.inventree.org/en/stable/extend/plugins/settings/
    SETTINGS = {
        # Define your plugin settings here...
        'CUSTOM_VALUE': {
            'name': 'Custom Value',
            'description': 'A custom value',
            'validator': int,
            'default': 42,
        }
    }
    
    
    
