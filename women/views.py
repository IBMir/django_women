from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    return HttpResponse('<H1>Главная страница сайта</H1>')


def categor(request, id):
    if id < 2023 and id > 1995:
        return HttpResponse(f'<H2>Категории</H2><p>{id}</p>')
    elif id > 2023:
        return redirect(f'https://yandex.ru/search/?text=архив+{id}+год&lr=213')
    else:
        return HttpResponse(f'<H2>Архив отсутствует</H2><p>Год - {id}</p>')


def ya(request):
    return redirect('https://ya.ru/')
