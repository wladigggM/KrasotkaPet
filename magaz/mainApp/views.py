from django.core.paginator import Paginator
from django.db.models import Max
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import ListView, TemplateView

from cart.models import Cart
from cart.utils import get_cart_user, add_to_cart
from .forms import *
from .models import *


# Create your views here.


class Index(ListView):
    def get(self, request, *args, **kwargs):
        thirty_days_ago = timezone.now() - timezone.timedelta(days=30)
        new_items = Item.objects.filter(created_at__gte=thirty_days_ago)
        carts = get_cart_user(request)
        data = {
            'items': new_items,
            'carts': carts,
        }

        return render(request, 'index.html', data)

    def post(self, request, *args, **kwargs):
        return add_to_cart(request)


class About(TemplateView):
    template_name = 'about.html'


class Categorys(ListView):

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        carts = get_cart_user(request)
        data = {
            'categories': categories,
            'carts': carts
        }
        return render(request, 'category.html', data)


class Sales(ListView):
    template_name = 'sale.html'

    def get(self, request, *args, **kwargs):
        carts = get_cart_user(request)
        data = {
            'carts': carts
        }
        return render(request, 'sale.html', data)


class ItemsView(ListView):
    paginate_by = 8

    def get(self, request, *args, **kwargs):
        cat_items = Item.objects.filter(slug_name=self.kwargs['cat_slug'])
        cat_name = Category.objects.filter(slug_name=self.kwargs['cat_slug'])
        carts = get_cart_user(request)

        data = {
            'items': cat_items,
            'cat_name': cat_name[0],
            'carts': carts,
        }

        return render(request, 'home_linen.html', data)

    def post(self, request, *args, **kwargs):
        return add_to_cart(request)


class AboutItemView(ListView):
    template_name = 'about_item.html'
    context_object_name = 'items'

    def get(self, request, *args, **kwargs):
        queryset = Item.objects.filter(item_slug=self.kwargs['item_slug'], slug_name=self.kwargs['cat_slug'])
        item = Item.objects.filter(item_slug=self.kwargs['item_slug'], slug_name=self.kwargs['cat_slug'])
        carts = get_cart_user(request)

        data = {
            'queryset': queryset,
            'item': item[0],
            'carts': carts

        }

        return render(request, 'about_item.html', data)

    def post(self, request, *args, **kwargs):
        return add_to_cart(request)


class ReviewsListView(ListView):
    model = Reviews
    template_name = 'reviews.html'
    context_object_name = 'reviews'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AddReview()
        carts = get_cart_user(self.request)
        context['carts'] = carts
        return context

    def post(self, request, *args, **kwargs):
        form = AddReview(request.POST)
        if form.is_valid():
            try:
                form.instance.user = request.user
                form.save()
                return redirect('reviews-list')
            except Exception as e:
                print(e)  # Printing the exception for debugging purposes
        return self.get(request, *args, **kwargs)

    def get_queryset(self):
        return Reviews.objects.order_by('?')[:6]  # ДОБАВИТЬ В БД ID_USER


class SizeTable(TemplateView):
    def get(self, request, *args, **kwargs):
        carts = get_cart_user(request)

        data = {
            'carts': carts
        }

        return render(request, 'size_table.html', data)

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
