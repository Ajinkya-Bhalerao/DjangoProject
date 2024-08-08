from django.shortcuts import render
from django.http import HttpResponse


def testDemo(request):
    return HttpResponse("Hello world")