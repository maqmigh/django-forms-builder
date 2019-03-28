from __future__ import unicode_literals

from django.views.generic import TemplateView

try:
    from django.urls import re_path
except ImportError:
    # For Django 1.8 compatibility
    from django.conf.urls import url as re_path

from forms_builder.forms import views


urlpatterns = [
    re_path(r"(?P<slug>.*)/embed/$", TemplateView.as_view(template_name='forms/form_embed.html'), name="form_embed"),
    re_path(r"(?P<slug>.*)/sent/$", views.form_sent, name="form_sent"),
    re_path(r"(?P<slug>.*)/$", views.form_detail, name="form_detail"),
]
