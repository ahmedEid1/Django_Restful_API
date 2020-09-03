from django.shortcuts import render
from store.models import Product, ShoppingCart


# Create your views here.
def index(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'store/product_list.html', context)


def cart(request):
    return None


def show(request):
    return None