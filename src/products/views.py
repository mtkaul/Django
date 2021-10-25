from django.shortcuts import render
# Create your views here.

from .forms import RawProductForm, ProductForm
from .models import Product
# Create your views here.

def product_create_view(request):
    my_form = RawProductForm()
    if request.method == "POST":
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
        else:
            print(my_form.errors)

    context = {
        'form': my_form
    }
    return render(request, "products/product_create.html", context)
# def product_create_view(request):
#     # print(request.GET['title'])
#     # print(request.POST)
#     if request.method == "POST":
#         my_new_title = request.POST.get('title')
#         print(my_new_title)
#
#     context = {}
#     return render(request, "products/product_create.html", context)

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     "title": obj.title,
    #     "description": obj.description,
    # } or use follwing styles so that you don't have update html everytime you update
    context = {
        "object": obj
    }
    return render(request, "product/detail.html", context)