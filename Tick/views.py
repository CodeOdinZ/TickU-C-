from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def tests(request):
    return HttpResponse("Hello Guys!!!")
