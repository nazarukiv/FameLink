from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.template.loader import render_to_string

from popularpeople.models import People, Category

menu = [
    {"name": "About Us", "url": "about"},
    {"name": "Add Article", "url": "add_page"},
    {"name": "Contact Us", "url": "contact"},
    {"name": "Log In", "url": "login"}
]



cats_db = [
    {"id": 1, "name": "Sportsmen"},
    {"id": 2, "name": "Actors"},
    {"id": 3, "name": "Scientists"},
    {"id": 4, "name": "Musicians"},
    {"id": 5, "name": "Authors"},
    {"id": 6, "name": "Entrepreneurs"},
    {"id": 7, "name": "Politicians"},
    {"id": 8, "name": "Philanthropists"},
    {"id": 9, "name": "Inventors"},
    {"id": 10, "name": "Artists"},
    {"id": 11, "name": "Explorers"}
]

def index(request):
    posts = People.published.all()
    data = {
        'title': "Main Page",
        'menu': menu,
        'posts': posts,
        'cats_selected': 0
    }
    return render(request, 'popularpeople/index.html', context=data)

def show_post(request, post_slug):
    post = get_object_or_404(People, slug=post_slug)
    data = {'title': post.title,
            'menu': menu,
            'post': post,
            'cat_selected': 1,
            }

    return render(request, 'popularpeople/post.html', data)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Page Not Found</h1>")


def addpage(request):
    return HttpResponse("Add article")

def contact(request):
    return HttpResponse("Contact Us")

def login(request):
    return HttpResponse("Login")


def about(request):
    data = {'menu': menu}
    return render(request, 'popularpeople/about.html', data)



def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = People.published.filter(cat_id=category.pk)

    data = {
        'title': f'Category: {category.name}',
        'menu': menu,
        'posts': posts,
        'cat_selected': category.pk,
    }
    return render(request, 'popularpeople/index.html', context=data)


