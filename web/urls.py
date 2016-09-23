"""

            Urls
        A clean, elegant URL scheme is an important
    detail in a high-quality Web application.

    Django lets you design URLs however you want,
    with no framework limitations.
"""
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home)
]
