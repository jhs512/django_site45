from django.http import HttpResponse, HttpRequest

def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("안녕")
