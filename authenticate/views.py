from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import Group
from .forms import LoginForm
from django.contrib import messages

# Create your views here.
def login_view(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)  # Bind the form with POST data
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                # Redirect users based on their group membership
                if Group.objects.get(name='student') in user.groups.all():
                    return redirect('student')
                elif Group.objects.get(name='teacher') in user.groups.all():
                    return redirect('teacher')
                elif user.is_superuser:
                    return redirect('teacher')    
                # elif Group.objects.get(name='hod') in user.groups.all():
                #     return redirect('hod')
                # elif Group.objects.get(name='tutor') in user.groups.all():
                #     return redirect('tutor')
                # elif Group.objects.get(name='principal') in user.groups.all():
                #     return redirect('principal')
            else:
                messages.error(request,f"Sorry, Invalid user")
    return render(request, 'authenticate/login.html', {'form': form})
    
def logout_view(request):
    logout(request)
    return redirect('login')

