from django.shortcuts import render
from django.utils import timezone
from datetime import *

# Create your views here.
from myApp.models import Grades, Students


grade1 = Grades()
grade1.gname ="python04"
grade1.gdate = datetime(year=2020, month= 3, day = 22)
grade1.ggirlnum = 3
grade1.gboynum = 30

grade1.save()

# find all the objects
grades = Grades.objects.all()

# find one object
grade1 = Grades.objects.get(pk=1)
Grades.objects.get(gname="python04")

# modify
grade3= Grades.objects.get(gname="python04")
grade3.gname ="python044"
grade3.save()

# delete --数据库表里面的数据被删除了
grade3.delete()



# create
student1 = Students()
student1.sname ="HHH"
student1.sgender = False
student1.sage= 20
student1.scontend ="good girl"
student1.sgrade = grade1
student1.save()

# 直接通过班级创建学生了!!!!!
grade3.students_set.create(
    sname="HHH3",
    sgender=False,
    sage=20,
    scontend="good girl",
).save()
# find all
Students.objects.all()
# get all the students who are belong to grade3
stu48 = Students.objects.filter(sgrade=grade3)
grade3.students_set.all()

# find one
stu47 = Students.objects.get(sname="HHH")

# update
stu47.sname ="HHH-new"
stu47.save()

# delete . the real data from the table.
stu47() 

# get the forein objects
stu47.sgrade

Students.stuObj2.all()
# Students.stuObj.all()