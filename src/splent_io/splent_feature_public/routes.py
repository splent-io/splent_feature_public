from flask import render_template

from splent_io.splent_feature_public import public_bp
from splent_framework.services.service_locator import service_proxy

events_service = service_proxy("EventsService")


@public_bp.route("/")
def index():
    """Public landing page, rendered with the active theme/skin.

    Shows a few upcoming events if the events feature is installed (soft
    dependency — the home still works without it).
    """
    try:
        upcoming = events_service.list_published()[:3]
    except Exception:
        upcoming = []
    return render_template("public/index.html", upcoming=upcoming)
