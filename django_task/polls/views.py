from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.http import Http404
from django.template import loader
# Create your views here.


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', locals())


def result(request, question_id):
    response = f'You are looking at the results of question {question_id}:'
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse(f"You'are voting on question{question_id}")


def index(request):

    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    return render(request, 'polls/index.html', locals())

