from django.shortcuts import render
from django.http import HttpResponse
from . import main1
# Create your views here.

def index(request):
    row = main1.output()
    return HttpResponse(row)
            
