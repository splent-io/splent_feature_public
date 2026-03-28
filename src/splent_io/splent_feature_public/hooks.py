from splent_framework.hooks.template_hooks import register_template_hook
from flask import url_for


def public_scripts():
    return '<script src="' + url_for('public.assets', subfolder='dist', filename='public.bundle.js') + '"></script>'


register_template_hook("layout.scripts", public_scripts)
