from django.shortcuts import render
# function base view 

# ...........

#from django.http import HttpResponse

# Create your views here.

# def HomePageView(request):
#     return HttpResponse('Hello world')


# class base view 

# from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import post

class HomePageView(ListView):
    model = post
    template_name = "home.html"



class AboutPageView(ListView):
    template_name = "about.html"
    
    
