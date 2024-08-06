from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, customAuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:signup')
    else:
        form = CustomUserCreationForm

    context = {
        'form': form,

    }

    return render(request, 'signup.html', context)

def login(request):
    if request.method == 'POST':
        form = customAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            next_url = request.GET.get('next')
            # next 인자에 url이 있을 때 => '/articles/1/' or 'articles:index'
            # next 인자에 url이 없을 때 => None or 'articles:index'
            return redirect(next_url or 'articles:index')

            
    else:
        form = customAuthenticationForm()


    context = {
        'form':form,
    }

    return render(request, 'login.html', context)

def logout(request):
    auth_logout(request)

    return redirect('accounts:login')