#this is my views.py file

import imp
from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

    # params = {'name':'awanish','age':'19'}
    # return HttpResponse('''hello<div><a href="http://127.0.0.1:8000/about">aboutpage</a></div><div><a href="http://127.0.0.1:8000/removepunc">removepunc page</a></div><div><a href="http://127.0.0.1:8000/capitalize">capitalize</a></div><div><a href="http://127.0.0.1:8000/newlineremove">newlineremove page</a></div><div><a href="http://127.0.0.1:8000/spaceremove">spaceremove page</a></div><div><a href="http://127.0.0.1:8000/charcount">charcount page</a></div>''')

def about(request):
    return HttpResponse('''about to hello <div><h1>My Nane Is Awanish Maurya</h1></div><div><a href ='/'>back</a></div>''')

def analyze(request):
    #get the text
    text = request.POST.get('text','default')

    # checkbox value 
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcount = request.POST.get('charcount','off')
    



    #analyse the text
    if removepunc == "on":
        punctuations = '''!()-[]{ };:'"\,<>./?@$%^*&_~#'''
        analyzed =""
        for char in text:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Remove punctions','analyzed_text': analyzed}
        text = analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in text:
            analyzed = analyzed + char.upper()

        params = {'purpose':'Changed to uppercase','analyzed_text': analyzed}
        text = analyzed

    if extraspaceremover  == "on":
        analyzed = ""
        for index, char in enumerate(text):
            if not(text[index] == " " and text[index+1] == " "):
                analyzed = analyzed + char

        params = {'purpose':'Removed extra spaces from line','analyzed_text': analyzed}
        text = analyzed

    if charcount == "on":
        analyzed = ""
        index = 0
        for index in text:
            index = len(text)
            index = str(index)
            analyzed = index
        params = {'purpose':'Removed new line','analyzed_text': analyzed}
        text = analyzed
    
    if newlineremover == "on":
        analyzed = ""
        for char in text:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose':'Removed new line','analyzed_text': analyzed}
        text = analyzed

    if(removepunc != "on" and fullcaps != "on" and extraspaceremover  != "on" and charcount != "on" and newlineremover != "on"):
        return HttpResponse("error")
    # analyzed = text
    return render(request,'analyze.html',params)

# def capitalize(request):
#     return HttpResponse("capitalize<div><a href ='/'>back</a></div>")

# def newlineremove(request):
#     return HttpResponse("newlineremove<div><a href ='/'>back</a></div>")

# def spaceremove(request):
#     return HttpResponse("spaceremove<div><a href ='/'>back</a></div>")

# def charcount(request):
#     return HttpResponse("charcount<div><a href ='/'>back</a></div>")