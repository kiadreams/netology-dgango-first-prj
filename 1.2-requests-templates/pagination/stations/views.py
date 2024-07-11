from csv import DictReader

from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.conf import settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open(settings.BUS_STATION_CSV, encoding="utf-8") as csv_file:
        stations = list(DictReader(csv_file))
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    number_of_page = request.GET.get("page", 1)
    paginator = Paginator(stations, 10)
    page_of_stations = paginator.get_page(number_of_page)
    context = {
        'bus_stations': page_of_stations,
        'page': page_of_stations,
    }
    return render(request, 'stations/index.html', context)
