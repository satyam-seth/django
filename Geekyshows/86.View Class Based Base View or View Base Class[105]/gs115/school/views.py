from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .forms import ContactForm

# Create your views here.

def homefun(request):
    return render(request,'school/home.html')

class HomeClassView(View):
    def get(self,request):
        return render(request,'school/home.html')

################################################################

def aboutfun(request):
    context={'msg':'Welcome To GeekyShows Function Based View'}
    return render(request,'school/about.html',context)

class AboutClassView(View):
    def get(self,request):
        context={'msg':'Welcome To GeekyShows Class Based View'}
        return render(request,'school/about.html',context)

################################################################

def contactfun(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('Thamk You Form Submitted !!')
    else:
        form=ContactForm()
    return render(request,'school/contact.html',{'form':form})

class ContactClassView(View):
    def get(self,request):
        form=ContactForm()
        return render(request,'school/contact.html',{'form':form})
    
    def post(self,request):
        form=ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('Thamk You Form Submitted !!')

#################################################################

# def newsfun(request):
#     context={'info':'CBI enquiry Why GeekyShows earns less Money'}
#     return render(request,'school/news.html',context)
def newsfun(request,template_name):
    template_name=template_name
    context={'info':'CBI enquiry Why GeekyShows earns less Money'}
    return render(request,template_name,context)

# class NewsClassView(View):
#     def get(self,request):
#         context={'info':'CBI enquiry Why GeekyShows earns less Money'}
#         return render(request,'school/news.html',context)
class NewsClassView(View):
    template_name=''
    def get(self,request):
        context={'info':'CBI enquiry Why GeekyShows earns less Money'}
        return render(request,self.template_name,context)