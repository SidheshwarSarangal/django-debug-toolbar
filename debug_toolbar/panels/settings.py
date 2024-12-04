from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.views.debug import get_default_exception_reporter_filter

from debug_toolbar.panels import Panel

# Use the safe settings filter to exclude sensitive settings
get_safe_settings = get_default_exception_reporter_filter().get_safe_settings

class SettingsPanel(Panel):
    """
    A panel to display all variables in django.conf.settings
    """
    # Path to the template used to render the panel content
    template = "debug_toolbar/panels/settings.html"

    # Mark this panel as asynchronous (optional, based on usage)
    is_async = True

    # The title of the panel in the Debug Toolbar
    nav_title = _("Settings")

    def title(self):
        # The title of the panel, which will appear in the toolbar
        return _("Settings from %s") % settings.SETTINGS_MODULE

    def generate_stats(self, request, response):
        # This method collects the settings data, filters out sensitive ones, 
        # and passes it to the template for rendering
        self.record_stats({"settings": dict(sorted(get_safe_settings().items()))})
s