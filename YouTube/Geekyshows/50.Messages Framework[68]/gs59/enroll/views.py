from django.shortcuts import render
from .forms import StudentRegistration
from django.contrib import messages
# Create your views here.

def regi(request):
    messages.info(request,'Now You can Login')
    messages.success(request,'Update ho gya hai')
    messages.warning(request,'This is warning')
    messages.error(request,'This is error')
    # for m in messages.get_messages(request):
    #     print(m)
    fm=StudentRegistration()
    return render(request,'enroll/userregistration.html',{'form':fm})