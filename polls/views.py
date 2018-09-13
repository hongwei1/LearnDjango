# https://docs.djangoproject.com/en/2.0/intro/tutorial01/#write-your-first-view

from django.http import HttpResponse

#This is callback function, need map this to a URL. and return HttpResponse. 
#to call the view, we need to map it to a URL - add for this we need a URLconf.
#you need create the `/Users/zhanghongwei/Documents/GitHub-Tower/LearnDjango/polls/urls.py` 
def index(request):
    return HttpResponse("Hello, world. You're at the polls index. ") 