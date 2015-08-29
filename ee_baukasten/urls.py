from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ee/(?P<ee_id>[0-9]+)$', views.ee_detail, name='ee_detail'),
    url(r'^effektgruppe/(?P<gruppe>[0-9]+)$', views.effektgruppe, name='effekt_gruppe'),
]