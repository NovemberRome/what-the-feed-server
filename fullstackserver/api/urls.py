from django.conf.urls import url
from . import views, views_feed

urlpatterns = [
    url(r'^login', views.login),
    url(r'^register', views.register),

    url(r'^feed/getmainfeed', views_feed.getMainFeed),
    url(r'^feed/addsubscription', views_feed.addSubscription),
    url(r'^feed/changesubscription', views_feed.changeSubscription),
    url(r'^feed/getfeed', views_feed.getFeed),
    url(r'^feed/deletesubscription', views_feed.deleteSubscription)
]