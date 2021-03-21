from django.shortcuts import render, redirect
from .froms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def original_view(request):
    return render(request, 'dragonapp/original.html')

def holmes_view_pk(request, pk):
    return render(request, 'dragonapp/holmes-pk.html')

def holmes_view(request):
    return render(request, 'dragonapp/holmes.html')

def login_view(request):
    user_form = LoginForm()

    content = {
        'user_form': user_form
    }
    return render(request, 'dragonapp/login.html', content)

def register_view(request):
    return render(request, 'dragonapp/register.html')

def index_view(request):
    return render(request, 'dragonapp/index.html')

def authors_view(request):
    return render(request, 'dragonapp/authors.html')

def author_view(request, pk):
    return render(request, 'dragonapp/author.html')

def books_view(request):
    return render(request, 'dragonapp/books.html')

def book_view(request, pk):
    return render(request, 'dragonapp/book.html')

def foreign_author(request):
    return render(request, 'dragonapp/foreignAuthor.html')

def test(request):
    return render(request, 'dragonapp/test.html')