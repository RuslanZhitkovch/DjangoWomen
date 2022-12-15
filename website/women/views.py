from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render,redirect
from .models import *

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]
def index(request):
    posts = Women.objects.all()
    return render(request,'women/index.html', {'posts' : posts, 'menu': menu, 'title': 'Главная страница'})

def categories(request, catid):
    return HttpResponse(f"Статьи по категориям {catid}")

def about(request):
    return render(request,"women/index.html", {'title': 'О сайте'})
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')