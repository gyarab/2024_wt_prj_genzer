from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def homepage_view(request):
    return render(request, 'main/homepage.html')