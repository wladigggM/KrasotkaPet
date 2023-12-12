from django.db.models import Max
from django.shortcuts import render, redirect
from random import randint as r
from .forms import *
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


def home_linen(request, cat_slug):
    categories = Category.objects.filter(slug_name=cat_slug)  # edit
    items = Item.objects.filter(slug_name=cat_slug)  # edit
    data = {
        "categories": categories,
        "items": items
    }
    return render(request, 'home_linen.html', data)


def reviews(request):
    global reviews
    if request.method == 'POST':
        form = AddReview(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('reviews')
            except:
                pass
    else:
        form = AddReview()
        reviews = Reviews.objects.order_by('?')[:5]
    return render(request, 'reviews.html', {'form': form, 'reviews': reviews, })
