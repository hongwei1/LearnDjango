# from django.http import HttpResponseRedirect
# from django.shortcuts import get_object_or_404, render
# from django.urls import reverse
# from django.views import generic
#
# from .models import Choice, Question
#
#
# class IndexView(generic.ListView):
#     template_name = 'polls/index.html'
#     # As to ListView ,it will provide the default context = question_list.
#     # so we need manully define the context_object_name.
#     context_object_name = 'latest_question_list'
#
#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Question.objects.order_by('-pub_date')[:5]
#
#
# class DetailView(generic.DetailView):
#     #question 是数据库表名字,会自动提供一个 context 变量给 template 用; It is question.
#     model = Question
#     #可以区分,DetailView 和ResultsView 是两个Html,但是相同的后端.
#     template_name = 'polls/detail.html'
#
#
# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'polls/results.html'
#
#
# def vote(request, question_id):
#     ... # same as above, no changes needed.