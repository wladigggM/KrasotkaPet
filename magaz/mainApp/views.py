from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def category(request):
    return render(request, 'category.html')


def sale(request):
    return render(request, 'sale.html')
