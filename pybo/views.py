from django.core.paginator import Paginator
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import QuestionForm, AnswerForm
from .models import Question


def index(request: HttpRequest) -> HttpResponse:
    page = request.GET.get('page', '1')

    question_list = Question.objects.order_by('-id')

    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    return render(request, "pybo/question_list.html", {
        "question_list": page_obj
    })


def detail(request: HttpRequest, question_id: int) -> HttpResponse:
    # question = Question.objects.get(id=question_id)
    question: Question = get_object_or_404(Question, id=question_id)

    return render(request, "pybo/question_detail.html", {
        "question": question
    })


def answer_create(request: HttpRequest, question_id: int) -> HttpResponse:
    question: Question = get_object_or_404(Question, id=question_id)

    if request.method == "POST":
        form: AnswerForm = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form: AnswerForm = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)


def question_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form: QuestionForm = QuestionForm(request.POST)

        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form: QuestionForm = QuestionForm()

    return render(request, 'pybo/question_form.html', {'form': form})
