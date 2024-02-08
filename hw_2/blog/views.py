from django.shortcuts import render
from .models import Article


def get_article_details(request, pk):
    articles = Article.objects.get(id=pk)
    return render(request, 'blog/article_details.html', {'articles': articles})

def get_article_index_page(request):
    articles = Article.objects.all()
    return render(request, 'blog/article_index.html', {'articles': articles})
