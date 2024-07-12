from django.shortcuts import render, reverse

DATA = {
    'Омлет': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'Макароны': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'Сливочное масло': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
    "Хлеб": {},
    "Помидоры": {'помидор, ломтик': 3},
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
        for (ingredient, amount) in DATA.get(dish, {}).items()
    }
    return {"recipe": products, "back": reverse("home")}


def show_recipes(request):
    pages = {dish: f"/{dish}" for dish in DATA}
    context = {"pages": pages}
    return render(request, "calculator/home.html", context)


def get_dishes(request, dish):
    context = add_servings(dish, request)
    return render(request, "calculator/index.html", context)
