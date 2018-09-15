# https://docs.djangoproject.com/en/2.0/intro/tutorial01/#write-your-first-view
from typing import Dict

from django.db.models import QuerySet
from django.http import HttpResponse
from django.template import loader

#This is callback function, need map this to a URL. and return HttpResponse. 
#to call the view, we need to map it to a URL - add for this we need a URLconf.
#you need create the `/Users/zhanghongwei/Documents/GitHub-Tower/LearnDjango/polls/urls.py` 

# Hard code htlm in view
# def index(request):
#     lasest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([])
#     return HttpResponse("Hello, world. You're at the polls index. ") 


def index(request):
    lasest_question_list = Question.objects.order_by('-pub_date')[:5]
    # the code loads template call `polls/index.html` and passes it a context
    # the context is a dictionart mapping template variable names to Python objects
    template = loader.get_template('polls/index.html')
    # this is just a dictionary mapping tempalte variable names to Python objects
    context: Dict[str, QuerySet[Question]] = {
        'lasest_question_list': lasest_question_list,
    }
    return HttpResponse(template.render(context, request)) 

#https://docs.djangoproject.com/en/2.0/topics/http/shortcuts/#django.shortcuts.render
from django.shortcuts import render
# the same as index, but with shortcut: render()
# load a template --> fill a context --> return HttpResponse object ==> render()
def index2(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context) # no need load template and reneter it by it .


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

# the view only do two things: HttpResponse or an exception Http404. 
def detail_old(request, question_id ):
    return HttpResponse("You are looking at question %s." % question_id)

from django.http import Http404
from django.shortcuts import render

from .models import Question
# ...
def detail_old2(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist !!!!!!!!!!!!!!!!!!!!!!!!!!!")
    return render(request, 'polls/detail.html', {'question': question})

from django.shortcuts import get_object_or_404, render
from .models import Question
# ...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "you are looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s." % question_id)