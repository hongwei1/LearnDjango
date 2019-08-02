from django.urls import path

from django.urls import path

from . import views
app_name = 'polls' # this is a Namespaing URL names. 这个 URL 有命名空间的.可以通过这个调用下面的 views

# 开始重构,改良代码
urlpatterns = [
    # IndexView 是继承自ListView. 所以用 as_view 调用就行了.不能调用自己的.
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

#Old Style,没有模板,没有道路
# urlpatterns = [
#     # this is a path from `django.urls`, URLconf stuff.
#     # the path is passed 4 arguments:
#     # route  -> string, contains a URL pattern.
#     # view   -> it is the function, with HttpRequest object as first argument, and any arguments.
#     # kwargs -> Arbitrary keyword arguments can be passed in a dirctionry to the target view.
#     # name   -> Naming your URL lets you refer to it unambiguously from elsewhere in Django.
#     # ex: /polls/
#     path('', views_old.index, name="index"),
#     # path('', views.index, name="index"),
#
#     # :question_id> --> defines the name that will be used to identify the matched pattern
#     # <int: --> part is a converter that dermines what patterns should mathc this part of he URL path
#     # no need cruft, such as .html, unless you want to.
#     # ex: /polls/5/ --> 司机说.view.detail_old 就是 python 的函数,函数的参数是通过这一步实现的.参数来自与 URL.
#     path('<int:question_id>/', views_old.detail, name='detail'),
#     # path('<int:question_id>/', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     path('<int:question_id>/results/', views_old.results, name='results'),
#     # ex: /polls/5/vote/
#     path('<int:question_id>/vote/', views_old.vote, name='vote'),
#
#     # ex:/polls/mineOwnPratice/
#     path('mineOwnPratice', views_old.mineOwnPratice, name="mineOwnPratice"),
# ]
