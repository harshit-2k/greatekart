from django.shortcuts import render
from store.models import Product,ReviewRating
def home(request):
    disp_products = Product.objects.all().filter(is_available=True).order_by('created_date')

     # get the reviews
    for product in disp_products:
        reviews = ReviewRating.objects.filter(product_id=product.id,status=True)

    context = {
        'disp_products':disp_products,
        'reviews':reviews,
    }
    return render(request,'home.html',context)

#def demo(request):
#   return render(request,'demo.html')