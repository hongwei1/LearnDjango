from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index2$', views.index2),
    # () 是组的意思,就会自动赋值给 detail的 parameters
    url(r'^(\d+)/$', views.detail),
    url(r'^(\d+)/(\d+)/$', views.detail2),
    url(r'^grades/$', views.grades),
    path('grades/<int:pk>', views.grade),
    url(r'^students/$', views.students),
    path('students/<int:pk>', views.student),
]
