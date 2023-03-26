# I have created this file - Satyam Seth
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext=request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    newlineremover=request.GET.get('newlineremover','off')
    extraspaceremover=request.GET.get('extraspaceremover','off')
    charactercounter=request.GET.get('charactercounter','off')
    if removepunc=='on':
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=''
        for char in djtext:
            if char not in punctuations:
                analyzed+=char
        djtext=analyzed
        # params={'purpose':'Remove Punctuations','analyzed_text':analyzed}
        # return render(request,'analyze.html',params)
    if newlineremover=='on':
        analyzed=''
        for char in djtext:
            if char!='\n':
                analyzed+=char
        djtext=analyzed
        # params={'purpose':'Remove New Lines','analyzed_text':analyzed}
        # return render(request,'analyze.html',params)
    if extraspaceremover=='on':
        analyzed=''
        for index,char in enumerate(djtext):
            if not (djtext[index]==' ' and djtext[index+1]==''):
                analyzed+=char
        djtext=analyzed
        # params={'purpose':'Extra Space Remove','analyzed_text':analyzed}
        # return render(request,'analyze.html',params)
    if fullcaps=='on':
        analyzed=''
        for char in djtext:
            analyzed+=char.upper()
        djtext=analyzed
        # params={'purpose':'Changed To Uppercase','analyzed_text':analyzed}
        # return render(request,'analyze.html',params)
    params={'purpose':'Analyzed','analyzed_text':djtext}
    return render(request,'analyze.html',params)
    
    # elif charactercounter=='on':
    #     n=len(djtext)
    #     params={'purpose':'Character Counter','analyzed_text':f'Number of Character in your text is {n}'}
    #     return render(request,'analyze.html',params)
    # else:
    #     return HttpResponse('Error')