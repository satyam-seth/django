from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Student

# Create your views here.

class StudentDetailedView(DetailView):
    model=Student