from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Student

# Create your views here.

class StudentDetailedView(DetailView):
    model=Student
    template_name='school/student.html'
    context_object_name='stu'
    # pk_url_kwarg='id'
    pk_url_kwarg='geek'