# I have created this file - Satyam Seth
from django.http import HttpResponse

def index(request):
    return HttpResponse('''<h1>Home</h1><a href="http://127.0.0.1:8000/removepunc">remove punc</a></br>
                                        <a href="http://127.0.0.1:8000/capitalizefirst">capatilize first</a></br>
                                        <a href="http://127.0.0.1:8000/newlineremove">newlineremove</a></br>
                                        <a href="http://127.0.0.1:8000/spaceremove">spaceremove</a></br>
                                        <a href="http://127.0.0.1:8000/charcount">charcount</a>''')

def removepunc(request):
    return HttpResponse('<h1>remove punc</h1><a href="http://127.0.0.1:8000/">Back</a>')

def capfirst(request):
    return HttpResponse('<h1>capatilize first</h1><a href="http://127.0.0.1:8000/">Back</a>')

def newlineremove(request):
    return HttpResponse('<h1>newlineremove</h1><a href="http://127.0.0.1:8000/">Back</a>')

def spaceremove(request):
    return HttpResponse('<h1>spaceremove</h1><a href="http://127.0.0.1:8000/">Back</a>')

def charcount(request):
    return HttpResponse('<h1>charcount</h1><a href="http://127.0.0.1:8000/">Back</a>')