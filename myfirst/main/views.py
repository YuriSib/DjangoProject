from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<head><meta name="yandex-verification" content="59d46a858fee7816" /></head>'
                        '<h4>Главная</h4>')

def about(request):
    return render(request, 'main/yandex_59d46a858fee7816.html')