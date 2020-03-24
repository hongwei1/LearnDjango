from django.db import models

# Create your models here.
class Grades(models.Model):
    gname = models.CharField(max_length=20)
    gdate = models.DateTimeField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isdelete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.gname


    
class Students(models.Model):
    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    sage = models.IntegerField()
    scontend = models.CharField(max_length=20)
    isdelete = models.BooleanField(default=False)
    # 关联外键,都不需要定义主键, 再生成时自动添加, 并且值为自动增加. 
    sgrade = models.ForeignKey(
        "Grades",
        on_delete=models.CASCADE) #Since Django 2.x, on_delete is required.
    def __str__(self):
        return self.sname

