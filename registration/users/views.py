from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm



# Create your views here.
def home(request):
    return render(request, 'users/home.html')
def about(request):
    return render(request, 'users/about.html')

def contact(request):
    return render(request, 'users/contact.html')

def login_view(request):
    return render(request, 'users/login.html')

def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Hi{username}')
            return redirect('home')
    else:
        form=UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})
    
