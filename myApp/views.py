from django.shortcuts import render
from django.utils import timezone
from datetime import *

# Create your views here.
from myApp.models import Grades, Students
from django.http import HttpResponse
# view 介于 template 和数据库 之间的... 其实就是个函数..
#从 get HttpRequest return HttpResponse just do this..
# know what it need from the httpRequest, and prepare the response for the httpResponse

# request is the browser give this parameter to backend server .
# 配置 URL
# 1st: 修改 mysite urls.py
# 2st: 创建 myApp urls.py
def index(request):
    return HttpResponse("Hello world!!!")

def detail(request, num):
    return HttpResponse("detail-%s"%num)

def detail2(request, num1, num2):
    return HttpResponse("detail---%s---%s"%(num1,num2))