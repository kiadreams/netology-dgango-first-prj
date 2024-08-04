from datetime import date

from django.shortcuts import render, redirect

from books.models import Book


def index(request):
    return redirect('books')


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {"books": books, "date_ls": None, "date_gt": None}
    return render(request, template, context)


def book_of_pub_date(request, pub_date):
    template = 'books/books_list.html'
    some_date = date.fromisoformat(pub_date)
    bks = Book.objects.all()
    date_ls = bks.filter(pub_date__lt=some_date).last()
    date_gt = bks.filter(pub_date__gt=some_date).first()
    books = bks.filter(pub_date=pub_date).all()
    context = {"books": books, "date_ls": date_ls, "date_gt": date_gt}
    return render(request, template, context)
