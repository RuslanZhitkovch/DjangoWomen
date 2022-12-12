from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def index(request):
    return HttpResponse("<h1>Главная страница сайта</h1>")

def categories(request, catid):
    return HttpResponse(f"Статьи по категориям {catid}")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')