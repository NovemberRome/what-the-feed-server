from django.conf.urls import url
from . import views, views_feed

urlpatterns = [
    url(r'^login', views.login),
    url(r'^register', views.register),
    url(r'^feed/getmainfeed', views_feed.getMainFeed)
]