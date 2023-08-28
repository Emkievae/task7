from django.shortcuts import render
# подключаем объект для выполнения http запросов
from django.http import HttpResponse

# Create your views here.

# ф-ция отображающая index.html
def index(request):
    return render(request, 'index.html')

def top_sellers(request):
    return render(request, 'top-sellers.html')