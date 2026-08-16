from flask import render_template

from splent_io.splent_feature_public import public_bp


@public_bp.route("/")
def index():
    """Public landing page, rendered with the active theme/skin.

    The shell knows nothing about content features. Each of them contributes
    its own section through the ``home.section`` slot (upcoming events,
    partners, latest photos…) and, when one owns the headline moment, the
    whole hero through ``home.hero``. What is left here is the product's
    brand copy from SITE_* config.
    """
    return render_template("public/index.html")
