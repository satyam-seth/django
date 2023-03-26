from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.

def showformdata(request):
    # fm=StudentRegistration()
    # fm=StudentRegistration(auto_id='some_%s')
    # fm=StudentRegistration(auto_id='geeky')
    # fm=StudentRegistration(auto_id=False)
    # fm=StudentRegistration(auto_id=True)
    # fm=StudentRegistration(auto_id=True,label_suffix='')
    # fm=StudentRegistration(auto_id=True,label_suffix=' ')
    # fm=StudentRegistration(auto_id=True,label_suffix='-')
    fm=StudentRegistration(auto_id=True,label_suffix='-',initial={'name':'Sonam','email':'sonam@gmail.com'})
    return render(request,'enroll/userregistration.html',{'form':fm})