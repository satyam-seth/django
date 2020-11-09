from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.

def showformdata(request):
    fm=StudentRegistration()
    # fm.order_fields(field_order=None)
    fm.order_fields(field_order=['email','name','first_name'])
    return render(request,'enroll/userregistration.html',{'form':fm})