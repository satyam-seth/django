from django.shortcuts import render,HttpResponse
from django.template.response import TemplateResponse

# Create your views here.

def home(request):
    print('I am View')
    return HttpResponse('This is Home Page')