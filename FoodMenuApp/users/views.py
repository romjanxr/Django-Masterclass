from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from users.forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


# Create your views here.

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username} your account has successfully created')
            return redirect('food:index')
        
    return render(request, 'users/register.html', {'form': form})


def login_user(request):
    form = AuthenticationForm()
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, "Username and password do not match")
            return render(request, 'users/login.html', {'form': form})

        login(request, user)
        messages.success(request, f'Welcome {username} login successfull')
        return redirect('food:index')
    return render(request, 'users/login.html', {'form': form})


def logout_user(request):
    username = request.user
    messages.success(request, f'{username} logged out successfully')
    logout(request)
    return redirect("food:index")

def pass_change(request):
    form = PasswordChangeForm(request.user)

    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.cleaned_data['user'])
            return redirect('profile')
    return render(request, 'users/pass_change.html', {'form': form})

