from django.shortcuts import render, get_object_or_404
from Categories.models import Category
from .models import Product, Brand


# Create your views here.
def home_pageview(request):
    
    brands=Brand.objects.all()
    categories=Category.objects.all()
    products= Product.objects.all()
    
    
    
    context = {
        'brands':brands,
        'categories':categories,
        'products':products
    }
    
    return render(request,'index.html',context)


def products_list(request, category_slug=None, brand_slug=None):
    category=None
    brand=None
    
    categories=Category.objects.all()
    brands=Brand.objects.all()
    products=Product.objects.filter(is_active=True)
    
    if category_slug:
        category=get_object_or_404(Category, slug=category_slug)
        products=Product.objects.filter(category=category)
        
    if brand_slug:
        brand=get_object_or_404(Brand, slug=brand_slug)
        products=Product.objects.filter(brand=brand)
        
        
    context={
        'brand':brand,
        'brands':brands,
        'category':category,
        'categories':categories,
        'products':products
    }
    return render(request,"product-list.html", context)
    
        

def product_detail(request,id,product_slug):
    product=get_object_or_404(Product,id=id, slug=product_slug, is_active=True)
    context={
        'product':product
    }
    
    return render(request, "product-detail.html",context)
    
    
    
    
    
    
    