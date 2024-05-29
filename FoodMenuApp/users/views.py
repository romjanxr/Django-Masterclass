from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from users.forms import RegistrationForm


# Create your views here.

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username} your account has successfully created')
            return redirect('food:index')
        
    return render(request, 'users/register.html', {'form': form})
