from django.http import request, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages
# from PIL import Image
from .models import product

# Create your views here.
def index(request):
    context = {
        "all_products" : product.objects.all()
    }
    if(request.POST.get('sort') == '/AtoZ'):
        prod = product.objects.all()
        context = {
            "all_products" : prod.order_by('title')
        }
    if(request.POST.get('sort') == '/LowtoHigh'):
        context = {
            "all_products" : product.objects.all().order_by('price')
        }
    return render(request, 'index.html', context)

def product_desc(request, product_id):
    # prod = product.objects.get(id=product_id)
    # image = Image.open(prod.image)
    context = {
        "product" : product.objects.get(id=product_id),
        # "img" : image
    }
    return render(request, 'product.html', context)

def product_edit(request, product_id):
    prod = product.objects.get(id=product_id)
    # image = Image.open(prod.image)
    context = {
        "edit_product" : prod,
        # "img" : image
    }
    return render(request, 'edit.html', context)

def edit_product(request):
    errors = product.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/product/new')
    s = product.objects.get(id=request.POST['product_id'])
    s.title = request.POST['title']
    s.desc = request.POST['desc']
    s.price = request.POST['price']
    s.quantity = request.POST['quantity']
    s.image = request.POST['image']
    s.save()
    num = request.POST['product_id']
    return HttpResponseRedirect(reverse('product_desc', args=(num,)))

def product_add(request):
    return render(request, 'add.html')

def add_a_product(request):
    errors = product.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/products/new')
    s = product.objects.create(
        title = request.POST['title'], 
        desc = request.POST['desc'], 
        price = request.POST['price'],
        quantity = request.POST['quantity'],
        image = request.POST['image'])
    num = s.id
    return HttpResponseRedirect(reverse('product_desc', args=(num,)))

def product_delete(request, product_id):
    s = product.objects.get(id=product_id)
    s.delete()
    return redirect('/')
