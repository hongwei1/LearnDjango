from django.urls import path

from . import views

# this just a normal variable
urlpatterns = [
    # this is a path from `django.urls`, URLconf stuff.
    # the path is passed 4 arguments: 
    # route  -> string, contains a URL pattern.
    # view   -> it is the function, with HttpRequest object as first argument, and any arguments.
    # kwargs -> Arbitrary keyword arguments can be passed in a dirctionry to the target view.
    # name   -> Naming your URL lets you refer to it unambiguously from elsewhere in Django.
    path('', views.index, name="index")
]
