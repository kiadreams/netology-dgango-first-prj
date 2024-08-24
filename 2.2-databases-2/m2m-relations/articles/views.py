from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    context = {}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'
    object_list = Article.objects.order_by(ordering).all()
    # for article in object_list:
    #     print(dir(article.scopes))
    #     print()
    #     print(type(article))
    #     for scope in article.scopes.all():
    #         print(type(scope))
    #         print(scope.name)
    #     break

    context['object_list'] = object_list

    return render(request, template, context)
