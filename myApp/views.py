from django.db.models import Max, F, Q
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
    grades = Grades.objects.all()[0:4]
    template = loader.get_template('myApp/grades.html') # we get this template from frontend
    grades = Grades.objects.filter(ggirlnum__exact = F('gboynum'))
    grades = Grades.objects.filter(Q(ggirlnum__gt =30) | Q(gboynum__gt =30) )
    grades = Grades.objects.filter(Q(ggirlnum__gt =30) )
    grades = Grades.objects.filter(~Q(ggirlnum__gt =30) )
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
    print(Grades.objects.all())
    print(Grades.objects.values())
    print(Grades.objects.filter(students__sname__contains ="H2"))
    
    return HttpResponse(template.render(context, request)) # then we can return this to the Django .return the request and the context    


def students(request):
    students = Students.objects.all()
    # students = Students.objects.filter(pk__in = [2,4,6])
    # students = Students.objects.filter(pk__gt = 5)
    # students = Students.objects.filter(pk__gte = 2)
    # students = Students.objects.filter(pk__lte = 2)
    # students = Students.objects.filter(pk__lt = 2)
    # students = Students.objects.filter(lastTime__year = 2020)
    # students = Students.objects.filter(lastTime__month = 5)
    # students = Students.objects.filter(lastTime__day = 5)
    # students = Students.objects.filter(lastTime__week_day= 5)
    # students = Students.objects.filter(lastTime__hour= 5)
    # students = Students.objects.filter(lastTime__minute= 5)
    # students = Students.objects.filter(lastTime__second= 5)
    
    return render(request, 'myApp/students.html', {
        'students': students
    })

def studentsPage(request, pageString):
    # 0-5 6-10 11- 15
    # 5*(page-1)*5: page*5
    page = int(pageString)
    students = Students.objects.all()[(page-1)*5: page*5]
    return render(request, 'myApp/students.html', {
        'students': students
    })

def student(request, pk):
    student = Students.objects.get(pk=pk)
    print(student.sgrade_id)
    print(student.sgrade)
    t73 =Students.objects.get(sname__exact="H4")
    t74 = Students.objects.filter(sname__contains="H4")
    t74 = Students.objects.filter(sname__icontains="H4")
    t75 = Students.objects.filter(sname__isnull=False)
    students = Students.objects.filter(pk__in = [2,4,6])
    # print(Students.objects.get(sname="h65"))
    # print(Students.objects.get(sname="h65131"))
    # student = Students.objects.aggregate(Max('sage'))
    return render(request, 'myApp/student.html', {
        'student': student
    })

def createstudent(request):
    student = Students.createStudent("h65",12,True, datetime(year=2020, month= 3, day = 22), datetime(year=2020, month= 3, day = 22))
    return render(request, 'myApp/student.html', {
        'student': student
    })

def createstudent2(request):
    student = Students.stuObj2.createStudent("h65",12,True, datetime(year=2020, month= 3, day = 22), datetime(year=2020, month= 3, day = 22)) 
    return render(request, 'myApp/student.html', {
        'student': student
    })