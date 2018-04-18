"""
    Urls

    A clean, elegant URL scheme is an important
    detail in a high-quality Web application.

    Django lets you design URLs however you want,
    with no framework limitations.
"""
from django.conf.urls import url
from blog import views


urlpatterns = [
    url(r'^$', views.BlogListView.as_view(), name='blog_home'),
    url(r'^(?P<pk>[0-9]+)/$',
        views.BlogDetailView.as_view(), name='blog_detail')
]
