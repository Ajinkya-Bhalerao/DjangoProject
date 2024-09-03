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
def singleUser(request, pk):
    try:
        user  = UserDetails.objects.get(pk=pk)
    except user.DoesNotExist:
        return JsonResponse({'error': 'User does not exist'},status=404)
    
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = UserSerializer(user, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse({'message': 'User deleted successfully'}, status=204)
    else:
        return HttpResponse(status=405)
    
@csrf_exempt    
def signup_new(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'login.html', {'form': form})
    else:
        form = SignUpForm()
        
    return render(request,'signup.html', {'form': form})

@csrf_exempt    
def login(request):
    if request.method == 'POST':
        
        return render(request, 'login.html')
    
    
    
