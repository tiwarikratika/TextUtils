# i have created this file - ktk


from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    return render(request, 'index.html')



def analyse(request):
    djtext = request.POST.get('text','default')

    #Check checkbox values
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremove','off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')

    #check which checkbox is on
    if removepunc == "on":
        punctuations = ''' !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ '''
        analysed = ""
        for char in djtext:
            if char not in punctuations:
                analysed = analysed + char
        params = {'purpose':'removed punctuations','analysed_text':analysed}
        return render(request, 'analyse.html',params)

    if fullcaps == "on":
        analysed = ""
        for char in djtext:
            analysed = analysed+ char.upper()
        params ={'purpose':'Changed to Upper case','analysed_text': analysed}
        return render(request, 'analyse.html', params)

    if newlineremove == "on":
        analysed = ""
        for char in djtext:
            if char != '\n' and char !='\r':
                analysed = analysed + char.upper()
        params = {'purpose':'New line removed', 'analysed text':analysed}
        return render(request,'analyse.html',params)

    elif spaceremover == "on":
        analysed = ""
        for char in djtext:
            if char != " ":
                analysed = analysed + char
        params = {'purpose': 'Spaces Removed', 'analysed_text': analysed}
        return render(request, 'analyse.html', params)

    if charcounter == "on":
        analysed = ""
        count=0
        for char in djtext:
            count=count+1
        analysed = count
        params = {'purpose': 'No of characters', 'analysed_text': analysed}
        return render(request, 'analyse.html', params)

    else:
        return HttpResponse("Error")


