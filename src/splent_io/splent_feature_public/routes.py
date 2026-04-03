import os
import sys
import platform

import flask
from flask import current_app, render_template

from splent_io.splent_feature_public import public_bp


@public_bp.route("/")
def index():
    # ── Product info ──────────────────────────────────────────────
    splent_app = os.getenv("SPLENT_APP", "unknown")
    splent_env = os.getenv("SPLENT_ENV", "unknown")

    # ── Features ──────────────────────────────────────────────────
    features = []
    blueprints = sorted(current_app.blueprints.keys())
    for bp_name, bp in sorted(current_app.blueprints.items()):
        entry = {"name": bp_name, "routes": 0}
        for rule in current_app.url_map.iter_rules():
            if rule.endpoint.startswith(f"{bp_name}."):
                entry["routes"] += 1
        features.append(entry)

    # ── Services ──────────────────────────────────────────────────
    services = sorted(getattr(current_app, "splent_services", {}).keys())

    # ── Runtime ───────────────────────────────────────────────────
    runtime = {
        "python": sys.version.split()[0],
        "flask": flask.__version__,
        "platform": platform.platform(),
        "debug": current_app.debug,
    }

    # ── Database ──────────────────────────────────────────────────
    db_url = current_app.config.get("SQLALCHEMY_DATABASE_URI", "")
    if "@" in db_url:
        db_display = db_url.split("@", 1)[1]
    else:
        db_display = db_url

    # ── Extensions ────────────────────────────────────────────────
    extensions = sorted(
        k
        for k in current_app.extensions.keys()
        if k not in ("splent_feature_commands", "splent_config_trace")
    )

    return render_template(
        "public/index.html",
        splent_app=splent_app,
        splent_env=splent_env,
        features=features,
        services=services,
        runtime=runtime,
        db_display=db_display,
        extensions=extensions,
        blueprints=blueprints,
    )
