from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def home(request):

    context = {"posts": Post.objects.all()}
    return render(request, "blog/home.html", context)


def about(reques):
    return render(reques, "blog/about.html", {"title": "wow"})


"""
to remembr
from django.http import HttpResponse
return HttpResponse('<h1>blog about</h1>')
"""

