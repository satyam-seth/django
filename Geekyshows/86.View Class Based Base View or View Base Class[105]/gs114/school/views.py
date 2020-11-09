from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# your views here.

# Function Based View
def myview(request):
    return HttpResponse('<h1>Function Based View</h1>')

# Class Based View
class MyView(View):
    # name=''
    name='Sonam'
    def get(self,request):
        # return HttpResponse('<h1>Class Based View - GET</h1>')
        return HttpResponse(self.name)

class MyViewChild(MyView):
    def get(self,request):
        return HttpResponse(self.name)