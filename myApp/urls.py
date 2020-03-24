from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    # () 是组的意思,就会自动赋值给 detail的 parameters
    url(r'^(\d+)/$', views.detail),
    url(r'^(\d+)/(\d+)/$', views.detail2)
]
