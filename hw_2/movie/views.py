from django.shortcuts import render
from .models import Film


def get_index_page(request):
    films = Film.objects.all()
    return render(request, 'movie/index.html', {'films': films})

def get_films_details(request, pk):
    films = Film.objects.get(id=pk)
    return render(request, 'movie/movie_details.html', {'films': films})


