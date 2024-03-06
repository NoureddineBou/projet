from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import User
from .models import CustomUserManager
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy



class CreateUser(CreateView):
    model = User
    fields = ['email', 'first_name', 'last_name', 'password']
    template_name = 'clients/create.html'
    success_url = reverse_lazy('profile')


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

