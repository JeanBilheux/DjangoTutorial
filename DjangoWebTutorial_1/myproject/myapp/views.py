from django.shortcuts import render
from django.http import HttpResponse

import datetime

# Create your views here.
def hello(request):
    today = datetime.datetime.now().date() 
    return render(request, 'myapp/hello.html', {'today': today})

def viewArticle(request, articleID):
    text = "Displaying article number: {}".format(articleID)
    return HttpResponse(text)

def viewArticles(request, month, year):
    text = "Displaying articles of {}/{}".format(month, year)
    return HttpResponse(text)