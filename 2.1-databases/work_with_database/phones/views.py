from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    phones = Phone.objects.all()
    if sort is None:
        context = {"phones": phones}
    elif sort == 'min_price':
        context = {"phones": phones.order_by("price")}
    elif sort == "max_price":
        context = {"phones": phones.order_by("-price")}
    else:
        context = {"phones": phones.order_by("name")}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {
        'phone': Phone.objects.get(slug=slug)
    }
    return render(request, template, context)
