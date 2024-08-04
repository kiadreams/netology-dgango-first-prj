from django.shortcuts import render, redirect

from books.models import Book

def index(request):
    return redirect('books')

def books_view(request):
    template = 'books/books_list.html'
    context = {
        "books": Book.objects.all(),
    }
    return render(request, template, context)
