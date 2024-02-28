from django.core.paginator import Paginator
from django.db.models import Max
from django.http import request
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import ListView, TemplateView
from .forms import *
from .models import *


# Create your views here.

class Index(ListView):

    def get(self, request, *args, **kwargs):
        thirty_days_ago = timezone.now() - timezone.timedelta(days=30)
        new_items = Item.objects.filter(created_at__gte=thirty_days_ago)

        return render(request, 'index.html', {'items': new_items})


class About(TemplateView):
    template_name = 'about.html'


class Categorys(ListView):
    model = Category
    template_name = 'category.html'
    context_object_name = 'categories'


class Sales(TemplateView):
    template_name = 'sale.html'


class ItemsView(ListView):
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        cat_items = Item.objects.filter(slug_name=self.kwargs['cat_slug'])
        cat_name = Category.objects.filter(slug_name=self.kwargs['cat_slug'])
        data = {
            'items': cat_items,
            'cat_name': cat_name[0],
        }

        return render(request, 'home_linen.html', data)


class AboutItemView(ListView):
    template_name = 'about_item.html'
    context_object_name = 'items'

    def get(self, request, *args, **kwargs):
        queryset = Item.objects.filter(item_slug=self.kwargs['item_slug'], slug_name=self.kwargs['cat_slug'])
        item = Item.objects.filter(item_slug=self.kwargs['item_slug'], slug_name=self.kwargs['cat_slug'])

        data = {
            'queryset': queryset,
            'item': item[0]

        }

        return render(request, 'about_item.html', data)


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
