from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from shop.models import Products

def index(request):
    item_name = request.GET.get('item_name')
    sort = request.GET.get('sort')

    if item_name:
        product_objects = Products.objects.filter(title__icontains=item_name)
    else:
        product_objects = Products.objects.all()

    # You can add sorting logic if you want:
    if sort == 'price_asc':
        product_objects = product_objects.order_by('price')
    elif sort == 'price_desc':
        product_objects = product_objects.order_by('-price')

    paginator = Paginator(product_objects, 4)  # 4 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'shop/index.html', {'product_objects': page_obj})

def detail(request, pk):
    product = get_object_or_404(Products, pk=pk)
    return render(request, 'shop/detail.html', {'product': product})

    