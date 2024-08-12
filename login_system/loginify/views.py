from django.shortcuts import render
from django.http import HttpResponse
from . models import UserDetails
from .serializers import UserSerializer
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from . forms import SignUpForm

# def testDemo(request):
#     return render(request, 'home.html')


@csrf_exempt
def userList(request):
    if request.method == 'GET':
        users = UserDetails.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt    
def signup_new(request):
    if request.method == 'POST':
        print(request.POST.get('username'))
        print(request.POST.get('email'))
        print(request.POST.get('password'))
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'login.html', {'form': form})
    else:
        form = SignUpForm()
        
    return render(request,'signup.html', {'form': form})

@csrf_exempt    
def login(request):

    if request.method == 'GET':
        return render(request, 'login.html')