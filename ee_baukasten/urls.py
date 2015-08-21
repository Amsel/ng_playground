from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ee/(?P<ee_id>[0-9]+)$', views.ee_detail, name='ee_detail'),
]