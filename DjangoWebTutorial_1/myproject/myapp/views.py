from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("<p>Hello World!</p>")

def viewArticle(request, articleID):
    text = "Displaying article number: {}".format(articleID)
    return HttpResponse(text)