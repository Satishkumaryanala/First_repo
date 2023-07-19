from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def first_response(request):
    return HttpResponse('This is first response')


def second_response(request):
    return HttpResponse('thi is Second response')

def third_response(request):
    return HttpResponse('This is third response')