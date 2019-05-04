from django.shortcuts import render
from magazine.models import Category,Product


def base_view(reques):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products
    }
    return render(reques, 'base.html', context)


def product_view(request, product_slug):
    product = Product.objects.get(slug = product_slug)
    categories = Category.objects.all()
    context = {
        'product': product,
        'categories': categories
    }
    return render(request,'product.html', context)

def category_view(request, category_slug):
    categories = Category.objects.all()
    category = Category.objects.get(slug = category_slug)
    products_of_category = Product.objects.filter(category=category)
    context = {
        'category': category,
        'products_of_category': products_of_category,
        'categories': categories
    }
    return render(request,'category.html', context)