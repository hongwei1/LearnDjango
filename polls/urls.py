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
    # ex: /polls/
    path('', views.index, name="index"),
    # ex: /polls/5/
    # :question_id> --> defines the name that will be used to identify the matched pattern
    # <int: --> part is a converter that dermines what patterns should mathc this part of he URL path
    # no need cruft, such as .html, unless you want to.
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    
    # ex:/poll/mineOwnPratice/
    path('mineOwnPratice', views.mineOwnPratice, name="mineOwnPratice"),
]
