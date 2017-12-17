from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse

def home_view(request):
    """Home view callable, for the home page."""
    template = loader.get_template("imager_profile/home.html")
    #response_body = template.render()
    return HttpResponse(template.render())
    #return HttpResponse('<h1>Hello World</h1>')

    
