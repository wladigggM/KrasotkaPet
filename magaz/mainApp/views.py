from django.shortcuts import render
from .models import *


# Create your views here.

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def category(request):
    categories = Category.objects.all()
    data = {
        "categories": categories
    }
    return render(request, 'category.html', data)


def sale(request):
    return render(request, 'sale.html')


def home_linen(request):
    categories = Category.objects.filter(name='Домашняя одежда')
    items = Item.objects.filter(category='1')
    data = {
        "categories": categories,
        "items": items
    }
    return render(request, 'home_linen.html', data)


def underwear(request):
    categories = Category.objects.filter(name='Нижнее белье')
    items = Item.objects.filter(category='2')
    data = {
        "categories": categories,
        "items": items
    }
    return render(request, 'underwear.html', data)


def socks(request):
    categories = Category.objects.filter(name='Носки')
    items = Item.objects.filter(category='3')
    data = {
        "categories": categories,
        "items": items
    }
    return render(request, 'socks.html', data)


def dresses(request):
    categories = Category.objects.filter(name='dresses')
    items = Item.objects.filter(category='4')
    data = {
        "categories": categories,
        "items": items
    }
    return render(request, 'socks.html', data)


def blouses(request):
    categories = Category.objects.filter(name='blouses')
    items = Item.objects.filter(category='5')
    data = {
        "categories": categories,
        "items": items
    }
    return render(request, 'socks.html', data)


def knitwear(request):
    categories = Category.objects.filter(name='knitwear')
    items = Item.objects.filter(category='6')
    data = {
        "categories": categories,
        "items": items
    }
    return render(request, 'socks.html', data)
