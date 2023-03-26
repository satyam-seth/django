from django.shortcuts import render
from django.db.models import Avg, Sum, Min, Max, Count
from datetime import date,time
from .models import Student

# Create your views here.

def home(request):
    student_data=Student.objects.all()
    average=student_data.aggregate(Avg('marks'))
    total=student_data.aggregate(Sum('marks'))
    minimum=student_data.aggregate(Min('marks'))
    maximum=student_data.aggregate(Max('marks'))
    totalcount=student_data.aggregate(Count('marks'))
    
    print(average)
    print(total)
    print(minimum)
    print(maximum)
    print(totalcount)

    context={'students':student_data,'average':average,'total':total,'minimum':minimum,'maximum':maximum,'totalcount':totalcount}
    
    print('Return:',student_data)
    print()
    print('SQL Query:',student_data.query)
    return render(request,'school/home.html',context)