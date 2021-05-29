from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index2.html")

def about(request):
    return HttpResponse("This is about")
def analyze(request):
    djText= request.POST.get('text','default')
    Removepunc = request.POST.get('rempunc', 'off')
    fullCapital = request.POST.get('Uppercase','off')
    NewLine= request.POST.get('newlinerem','off')
    SpaceRem = request.POST.get('spacerem', 'off')
    if Removepunc == "on":
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        newstr = ''
        for char in djText:
            if char not in punc:
                newstr = newstr+ char
        param= {'purpose':'Remove Punctuations','analyzed_text':newstr}
        djText = newstr

    if fullCapital == "on":
        newstr = djText.upper()
        param = {'purpose': 'Full Capitalize', 'analyzed_text': newstr}
        djText = newstr

    if NewLine == "on":
        newstr = ""
        for char in djText:
            if char!= "\n" and char!="\r":
                newstr = newstr+ char
        param = {'purpose': 'NewLineRemover', 'analyzed_text': newstr}
        djText= newstr

    if SpaceRem == "on":
        newstr = ""
        for index,char in enumerate(djText) :
           if not (djText[index]==" "and djText[index+1]==" "):
               newstr = newstr+char
        param = {'purpose': 'Space Remover', 'analyzed_text': newstr}
        djText= newstr
    if SpaceRem != "on" and NewLine != "on" and fullCapital != "on" and Removepunc!="on":
        return HttpResponse("Error")

    return render(request, 'analyze2.html', param)
def navigator(request):
    return render(request,'nav.html')