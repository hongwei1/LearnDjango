from django.db import models

# Create your models here.
# (model.Model) mean this Class is represented by a class that subclasses `django.db.model.Model`.

class Question(models.Model):
    #question_text is the field's name, same as the column name in database.
    question_text = models.CharField(max_length=200) 
    pub_date = models.DateTimeField('date published') # is a human-readable name. 
    def __str__(self):
        return self.question_text
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #BK 2 CASCADE mean??
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __self__(self):
        return self.choice_text