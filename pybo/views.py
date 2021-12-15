import string

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404

from .models import Question


def index(request: HttpRequest) -> HttpResponse:
    question_list = Question.objects.order_by('-id')

    return render(request, "pybo/question_list.html", {
        "question_list": question_list
    })


def detail(request: HttpRequest, question_id: int) -> HttpResponse:
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, id=question_id)

    return render(request, "pybo/question_detail.html", {
        "question": question
    })
