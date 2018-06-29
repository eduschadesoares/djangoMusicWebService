from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView

def home(request):
    return HttpResponse("Hello world")
