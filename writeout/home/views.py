from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect

def homeRedirect(request):
    return HttpResponseRedirect("/home")

def index(request):
    return render(request,'home/homePage.html')

def contact(request):
    return render(request,'home/contactPage.html')

