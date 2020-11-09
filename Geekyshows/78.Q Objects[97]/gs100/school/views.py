from django.shortcuts import render
from django.db.models import Q
from .models import Student

# Create your views here.

def home(request):
    # student_data=Student.objects.filter(Q(id=6) & Q(roll=106))
    # student_data=Student.objects.filter(Q(id=6) & Q(roll=107))
    
    # student_data=Student.objects.filter(Q(id=6) | Q(roll=107))
    
    student_data=Student.objects.filter(~Q(id=6))

    print('Return:',student_data)
    print()
    print('SQL Query:',student_data.query)
    return render(request,'school/home.html',{'students':student_data})