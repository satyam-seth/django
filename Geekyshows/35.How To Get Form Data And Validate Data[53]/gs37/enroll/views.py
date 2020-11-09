from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.

# def showformdata(request):
#     if request.method=='POST':
#         fm=StudentRegistration(request.POST)
#         print('ye POST request se aaya hai')
#         print(fm)
#         print('Cleaned_data:',fm.cleaned_data)
#         print('Name:',fm.cleaned_data['name'])
#         print('Email:',fm.cleaned_data['email'])
#     else:
#         fm=StudentRegistration()
#         print('ye GET request se aaya hai')
#     return render(request,'enroll/userregistration.html',{'form':fm})

def showformdata(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            print('Form Validated')
            # name=fm.cleaned_data['name']
            name=request.POST['name']
            email=fm.cleaned_data['email']
            password=fm.cleaned_data['password']
            print('Name:',name)
            print('Email:',email)
            print('Password:',password)
            fm=StudentRegistration()
    else:
        fm=StudentRegistration()
    return render(request,'enroll/userregistration.html',{'form':fm})