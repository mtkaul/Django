from django.shortcuts import render
# Create your views here.


from .models import Product
# Create your views here.
def product_create_view(request):
    # print(request.GET['title'])
    # print(request.POST)
    if request.method == "POST":
        my_new_title = request.POST.get('title')
        print(my_new_title)

    context = {}
    return render(request, "products/product_create.html", context)

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