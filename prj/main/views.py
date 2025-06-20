from django.shortcuts import render
from .models import Film

def homepage_view(request):
    # Get search query and genre filter from the request
    search_query = request.GET.get('search', '')
    genre_filter = request.GET.get('genre', '')

    # Filter films based on search query and genre
    films = Film.objects.all()
    if search_query:
        films = films.filter(nazev__icontains=search_query)
    if genre_filter:
        films = films.filter(zanr=genre_filter)

    # Get distinct genres for filtering
    genres = Film.objects.values_list('zanr', flat=True).distinct()

    context = {
        'films': films,
        'genres': genres,
        'genre': genre_filter,
    }
    return render(request, 'main/homepage.html', context)