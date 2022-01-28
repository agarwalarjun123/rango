from django.shortcuts import render
from .models import Category,Page


# Create your views here.

def index(request):
    category_list = Category.objects.all().order_by('-likes')[:5]
    pages_list = Page.objects.all().order_by('-views')[:5]
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = pages_list
    return render(request, 'rango/index.html', context_dict)
def show_category(request,category_name_slug):
    context_dict = {}
    category = None
    try:
        category = Category.objects.get(slug = category_name_slug)
    except Category.DoesNotExist:
        return render(request,'rango/category.html',context = context_dict)
    pages = Page.objects.filter(category = category)
    context_dict['pages'] = pages
    context_dict['category'] = category    
    return render(request, 'rango/category.html',context_dict)
def about(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/about.html', context_dict)
