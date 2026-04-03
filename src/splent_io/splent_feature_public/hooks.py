from splent_framework.hooks.template_hooks import register_template_hook
from flask import url_for


def home_sidebar_link():
    return (
        '<li class="sidebar-item">'
        f'<a class="sidebar-link" href="{url_for("public.index")}">'
        '<i class="align-middle" data-feather="home"></i> '
        '<span class="align-middle">Home</span>'
        "</a>"
        "</li>"
    )


register_template_hook("layout.sidebar.top", home_sidebar_link)
