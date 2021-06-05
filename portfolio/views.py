from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Project


def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})


def prechu(request):
    return render(request, 'portfolio/prechu.html')


def surfing(request):
    return render(request, 'portfolio/surfing.html')
