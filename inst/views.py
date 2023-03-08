from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse


# Create your views here.
def first(request):
    return HttpResponse('Login'),
def second(request):
    return HttpResponse('SignUp')   