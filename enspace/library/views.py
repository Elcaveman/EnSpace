from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def library_home_view(request):
    return HttpResponse("library")