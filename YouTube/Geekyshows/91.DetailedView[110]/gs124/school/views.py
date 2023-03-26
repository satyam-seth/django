from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Student

# Create your views here.

class StudentDetailedView(DetailView):
    model=Student
    template_name='school/student.html'

class StudentListView(ListView):
    model=Student