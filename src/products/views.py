from django.shortcuts import render
# Create your views here.


from .models import Product
# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        "title": obj.title,
        "description": obj.description,
    }
    return render(request, "product/detail.html", context)