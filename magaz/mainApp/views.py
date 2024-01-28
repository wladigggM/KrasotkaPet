from django.db.models import Max
from django.http import request
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .forms import *
from .models import *


# Create your views here.
# def index(request):
#     return render(request, 'index.html')
class Index(ListView):
    model = Category  # Тут должна быть модель с новинками
    template_name = 'index.html'


def about(request):
    return render(request, 'about.html')


class Categorys(ListView):
    model = Category
    template_name = 'category.html'
    context_object_name = 'categories'


#    extra_context = {'tittle': 'Категории'}

# def category(request):
#     categories = Category.objects.all()
#     data = {
#         "categories": categories
#     }
#     return render(request, 'category.html', data)


def sale(request):
    return render(request, 'sale.html')


class ItemsView(ListView):
    model = Item
    template_name = 'home_linen.html'
    context_object_name = 'items'
    paginate_by = 10

    def get_queryset(self):
        return Item.objects.filter(slug_name=self.kwargs['cat_slug'])


class AboutItemView(ListView):
    model = Item
    template_name = 'about_item.html'
    context_object_name = 'items'

    def get_queryset(self):
        item_slug = self.kwargs['item_slug']
        cat_slug = self.kwargs['cat_slug']

        queryset = Item.objects.filter(item_slug=item_slug, slug_name=cat_slug)
        return queryset


# def home_linen(request, cat_slug):
#     categories = Category.objects.filter(slug_name=cat_slug)  # edit
#     items = Item.objects.filter(slug_name=cat_slug)  # edit
#     data = {
#         "categories": categories,
#         "items": items
#     }
#     return render(request, 'home_linen.html', data)

class ReviewsListView(ListView):
    model = Reviews
    template_name = 'reviews.html'
    context_object_name = 'reviews'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AddReview()
        return context

    def post(self, request, *args, **kwargs):
        form = AddReview(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('reviews-list')
            except:
                pass
        return self.get(request, *args, **kwargs)

    def get_queryset(self):
        return Reviews.objects.order_by('?')[:6]  # ДОБАВИТЬ В БД ID_USER

# def reviews(request):
#     global reviews
#     if request.method == 'POST':
#         form = AddReview(request.POST)
#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect('reviews')
#             except:
#                 pass
#     else:
#         form = AddReview()
#         reviews = Reviews.objects.order_by('?')[:5]
#     return render(request, 'reviews.html', {'form': form, 'reviews': reviews, })
