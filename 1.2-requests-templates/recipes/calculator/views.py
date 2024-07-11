from django.shortcuts import render, reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'butter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
    "bread": {}
}


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
def add_servings(dish: str, request):
    portions = int(request.GET.get("servings", 1))
    products = {
        ingredient: amount * portions
        for (ingredient, amount) in DATA[dish].items()
    }
    return {"recipe": products, "back": reverse("home")}


def show_recipes(request):
    pages = {
        "Омлет": reverse("omlet"),
        "Макароны": reverse("pasta"),
        "Сливочное масло": reverse("butter"),
        "Хлеб": reverse("bread"),
    }
    context = {"pages": pages}
    return render(request, "calculator/home.html", context)


def get_omlet(request):
    context = add_servings("omlet", request)
    return render(request, "calculator/index.html", context)


def get_pasta(request):
    context = add_servings("pasta", request)
    return render(request, "calculator/index.html", context)


def get_butter(request):
    context = add_servings("butter", request)
    return render(request, "calculator/index.html", context)


def get_bread(request):
    context = add_servings("bread", request)
    return render(request, "calculator/index.html", context)
