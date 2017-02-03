from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "app_forum/home.html")

# def home(request):
#     return HttpResponse("This is the home view of the forum.")
