from django.shortcuts import render, get_object_or_404

from catalog.models import Product, Category


def home(request):
    products_list = Product.objects.all()
    context = {"products_list": products_list}
    return render(request, 'home.html', context)


def product(request, pk):
    product_ = get_object_or_404(Product, pk=pk)
    context = {"product": product_}
    return render(request, 'product.html', context)
