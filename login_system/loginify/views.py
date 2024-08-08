from django.shortcuts import render
from django.http import HttpResponse


def testDemo(request):
    return render(request, 'home.html')