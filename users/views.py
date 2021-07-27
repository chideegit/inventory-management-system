from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .form import RegisterUserForm


def RegisterUserView(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Account created. Please login.")
            return redirect('login')
    else:
        form = RegisterUserForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)


def LoginUserView(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('dashboard')
    else:
        messages.warning(request, 'Incorrect Login Details')
    return render(request, 'users/login.html')

def LogoutUserView(request):
    logout(request)
    return redirect('login')