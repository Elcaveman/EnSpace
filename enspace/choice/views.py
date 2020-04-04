from django.shortcuts import render
from . import models

# Create your views here.

def home_view(request):
    queryset = models.Application.objects.all()
    return render(request, "choice/main.html", {"Applications" : queryset})
    