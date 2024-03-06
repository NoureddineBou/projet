from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .models import user
from .models import CustomUserManager



def create(request):
    if request.method == 'POST':
        user = CustomUserManager()
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        print(username)
        data = user.create_user(username = username, password = password, email = email)
        print(username)
        if user is not None:
            if user.objects.filter(username=username).exists():
                    error_message = "Username already exists. Please choose a different username."
                    return render(request, 'clients/create.html', {'error_message': error_message})
            else:
                data.save()   
                error_message = ''
                user = user.objects.filter(username=username).first()
                login(request, user)
                return redirect('profile')
    if request.method == 'GET':
         return render(request, 'clients/create.html')  
    
    


def loginn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = user.objects.filter(username=username).first()
        print(user)
        error_message = None    
        if user is not None:

            try:
                if user.password == password:
                    login(request, user)
                    return redirect('profile') 
                else:
                    error_message = "Incorrect password."
            except:
                error_message = "Incorrect password."
        else:
            error_message = "Account does not exist."
        
        
        return render(request, 'clients/login.html', {'error_message': error_message})
    if request.method == "GET":
        return render(request, 'clients/login.html')
        
    
    


def view_profile(request):
    return render(request, 'clients/view_profile.html')


def home(request):
    return render(request, 'pages/index.html')

