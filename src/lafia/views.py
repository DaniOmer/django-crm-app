from django.shortcuts import render
from django.http import HttpResponse


def homepage_view(request, *args, **kwargs):
    return HttpResponse("<div>Welcome to Lafia Estate CRM</div>")