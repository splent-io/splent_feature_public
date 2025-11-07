from flask import render_template

from splent_io.splent_feature_public import public_bp


@public_bp.route("/")
def index():

    return render_template("public/index.html")
