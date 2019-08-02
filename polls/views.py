from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    # As to ListView ,it will provide the default context = question_list.
    # so we need manully define the context_object_name.
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    #question 是数据库表名字,会自动提供一个 context 变量给 template 用; It is question.
    model = Question
    #可以区分,DetailView 和ResultsView 是两个Html,但是相同的后端.
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:  # request.POST是一个类字典对象, 让你可以通过关键字的名字获取提交的数据.--> request.POST['choice'] 以字符串返回 Choice 的 ID.
        selected_choice: Choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        # reserse()函数避免了,我们在视图中用硬编码 URL
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))