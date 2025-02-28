from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from .models import Student

# Create your views here.

class StudentCreateView(CreateView):
    model=Student
    fields=['name','email','password']
    # success_url='/create/'
    # success_url='/thanks/'
    template_name='school/sform.html'

class ThanksTemplateView(TemplateView):
    template_name='school/thanks.html'

class StudentDetailView(DetailView):
    model=Student