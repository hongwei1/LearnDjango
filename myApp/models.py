from django.db import models


# Models 支持的各种类型
# 1: AutoField --> can not have more then one ..
# 2: Charfield --> 默认表达样式: TextInput
# 3: Textfield --> 默认是 Textarea, 一般超过4000使用, 
# 4: Integerfield
# 5: DecimalField
#     
# Create your models here.
class Grades(models.Model):
    gname = models.CharField(max_length=20)
    gdatetime = models.DateTimeField()
    gdate = models.DateField(null=True)
    gtime = models.TimeField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    gdescription = models.TextField() 
    isdelete = models.BooleanField(default=False)
    gfilefield = models.FileField()
    # gimagefield = models.ImageField()
    glasttime = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.gname
    class Meta:
        db_table="myapp_grade"
        ordering=['id'] # 会增加数据库的开销


class StudentsManager(models.Manager):
    def get_queryset(self):
        return super(StudentsManager, self).get_queryset().filter(isdelete= False) #可以加过滤条件.
    def createStudent(self, name, age, gender, lastTime, createTime, isdelete= False):
        grade = Grades.objects.get(pk=1)

        student  = self.model()
        student.sname =name
        student.sage=age
        student.sgender=gender
        student.lastTime= lastTime
        student.createTime =createTime
        student.sgrade=grade
        student.save()
        return student
    
class Students(models.Model):
    @classmethod
    def createStudent(cls, name, age, gender, lastTime ,createTime, isdelete= False):
        grade = Grades.objects.get(pk=1)

        student  = cls(sname =name, sage=age, sgender=gender, lastTime= lastTime, createTime =createTime, sgrade=grade)
        student.save()
        return student
    
    # 自定义模型管理器
    objects = models.Manager() # 会让 obejects 失效了.
    stuObj2 = StudentsManager() # 自己定义的 Manager.
    
    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    sage = models.IntegerField(db_column="ssage") # 默认就是字段名字:sage
    # spoints2 = models.FloatField()
    # spoints = models.DecimalField(
    #     max_digits = 5, # 最大不能超过5位
    #     decimal_places = 2) # 小数不能超过2位
    # scontend = models.CharField(max_length=20)
    isdelete = models.BooleanField(default=False) #只有 True 和 False 两种值.
    # isdelete2 = models.NullBooleanField() # Null, True 和 False 三种值.
    # # 关联外键,都不需要定义主键, 再生成时自动添加, 并且值为自动增加. 
    sgrade = models.ForeignKey( # 1 对 多
        "Grades",
        on_delete=models.CASCADE) #Since Django 2.x, on_delete is required.
    lastTime = models.DateTimeField(auto_now=True)
    createTime = models.DateTimeField(auto_now_add=True)
    # sgrade = models.ManyToManyField( # 多 对 多
    #     "Grades") #Since Django 2.x, on_delete is required.
    # 
    # sgrade = models.OneToOneField( # 1 对 1
    #     "Grades") #Since Django 2.x, on_delete is required.
    def __str__(self):
        return self.sname+str(self.sage)+str(self.lastTime)
    class Meta:
        db_table="myapp_student"
        ordering=['sname','-id'] 
        # ordering=['-id'] # 降序
        