from django.shortcuts import render
from django.template import loader
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


def index2(request):
    # you must set the myApp folder for the index.html file:
    # and as to the context, you can not find it 
    return render(request,"myApp/index.html",{"Test":"Good Boy!!!"})

def detail(request, num):
    return HttpResponse("detail-%s"%num)

def detail2(request, num1, num2):
    return HttpResponse("detail---%s---%s"%(num1,num2))

def grades(request):
    grades = Grades.objects.all()
    template = loader.get_template('myApp/grades.html') # we get this template from frontend
    context = {
        'grades': grades,
    } # then we can update the template by this object.
    # template 用 render 渲染 html要用context 和 request 两个 parameters.
    return HttpResponse(template.render(context, request)) # then we can return this to the Django .return the request and the context

def grade(request, pk):
    grade = Grades.objects.get(pk=pk)
    template = loader.get_template('myApp/grade.html') # we get this template from frontend
    context = {
        'grade': grade,
    } # then we can update the template by this object.
    # template 用 render 渲染 html要用context 和 request 两个 parameters.
    return HttpResponse(template.render(context, request)) # then we can return this to the Django .return the request and the context    


def students(request):
    students = Students.objects.all()
    return render(request, 'myApp/students.html', {
        'students': students
    })


def student(request, pk):
    student = Students.objects.get(pk=pk)
    return render(request, 'myApp/student.html', {
        'student': student
    })