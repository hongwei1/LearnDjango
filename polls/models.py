# This is the Python's standard datetime module.
import datetime
# 编辑 models.py 文件，改变模型。
# 运行 python manage.py makemigrations 为模型的改变生成迁移文件。
# 运行 python manage.py migrate 来应用数据库迁移。

from django.db import models
#THis is the Django's time-zone-realated utilities 
from django.utils import timezone

# Create your models here.
# (model.Model) mean this Class is represented by a class that subclasses `django.db.model.Model`.

class Question(models.Model):
    #question_text is the field's name, same as the column name in database.
    question_text = models.CharField(max_length=200) 
    pub_date = models.DateTimeField('date published') # is a human-readable name. 
    #this __str__ is not only for your own convenience when dealing with the interactive prompt.
    # but also because objects' representations are used throughout Django's automatically-generated admin.
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #BK 2 CASCADE mean??
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __self__(self):
        return self.choice_text