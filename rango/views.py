from django.urls import reverse
from django.shortcuts import redirect, render

from rango.forms import CategoryForm, PageForm
from .models import Category, Page

# Create your views here.

def index(request):
    category_list = Category.objects.all().order_by('-likes')[:5]
    pages_list = Page.objects.all().order_by('-views')[:5]
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = pages_list
    return render(request, 'rango/index.html', context_dict)


def show_category(request, category_name_slug):
    context_dict = {}
    category = None
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        return render(request, 'rango/category.html', context=context_dict)
    pages = Page.objects.filter(category=category)
    context_dict['pages'] = pages
    context_dict['category'] = category
    return render(request, 'rango/category.html', context_dict)


def about(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/about.html', context_dict)


def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/rango/')
        else:
            print(form.errors)

    return render(request, 'rango/add_category.html', {'form': form})


def add_page(request, category_name_slug):
    category = None
    form = PageForm()
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
       return redirect('/rango/')
    if request.method == 'POST':
        page = request.POST
        page = PageForm(page)
        if category and page.is_valid():
            page = page.save(commit=False)
            page.category = category
            page.save()
            return redirect(reverse('rango:show_category', kwargs={'category_name_slug': category_name_slug}))
        return render(request, 'rango/add_page.html', {"form": page, "category": category.__dict__})
    elif request.method == 'GET':
        return render(request, 'rango/add_page.html', {"form": form, "category": category.__dict__})
    else:
        return redirect('/rango/')
