# https://docs.djangoproject.com/en/2.0/intro/tutorial01/#write-your-first-view

from django.http import HttpResponse

#This is callback function, need map this to a URL. and return HttpResponse. 
#to call the view, we need to map it to a URL - add for this we need a URLconf.
#you need create the `/Users/zhanghongwei/Documents/GitHub-Tower/LearnDjango/polls/urls.py` 


def index(request):
    return HttpResponse("Hello, world. You're at the polls index. ") 

from polls.models import Question, Choice
from django.utils import timezone
# https://docs.djangoproject.com/en/2.0/intro/tutorial02/#playing-with-the-api
# I just want to have fun here, test some database apis.
def mineOwnPratice(request):
    current_year = timezone.now().year
    a19 = Question.objects.all()
    q= Question(question_text="What's new ?", pub_date=timezone.now())
    q.save()
    a22 = q.id
    a23 = q.pub_date
    a24 = q.question_text ="What's up?"
    a25 = q.save()
    a26 = Question.objects.all()
    #Django provies a rich database lookup API that's enritely driven by keyword arguments
    a28 = Question.objects.filter(id=1)
    a29 = Question.objects.filter(question_text__startswith='What')
    a30 = Question.objects.filter(pub_date__year=current_year)
    
    # shortcut for primary-key exact lookups.
    a32 = Question.objects.get(pk =1)
    a32.was_published_recently()
    
    #Foreign-Key, from Question -> Choice
    a37 =  a32.choice_set.all()
    a32.choice_set.create(choice_text="Not Much", votes=0)
    a32.choice_set.create(choice_text="The Sky", votes=0)
    a40: Choice = a32.choice_set.create(choice_text="Just Hacking again", votes=0)
    a40.question
    a32.choice_set.all()
    a32.choice_set.count()
    
    
    # The API automtically follows relationships as far as you need.
    # Use double underscores (__) to separate relationships. works ,as many as you want
    #eg: question.pub_date.year == question__pub_date__year in Django
    a49 = Choice.objects.filter(question__pub_date__year=current_year)
    
    #Delete one of the choices
    a52 = a32.choice_set.filter(choice_text__startswith="Just Hacking")
    a52.delete()
    
    
    
    
    
    return HttpResponse(a32) 