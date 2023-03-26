# I am created this file
from django.http import HttpResponse

with open('sample.txt','r') as f:
    text=f.read()

def home(request):
    return HttpResponse(text)