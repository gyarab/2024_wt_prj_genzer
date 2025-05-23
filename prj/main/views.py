from django.shortcuts import render
from django.http import HttpResponse

from main.models import Movie, Genre

def get_homepage(request):
    return render(
        request, "main/homepage.html"
    )