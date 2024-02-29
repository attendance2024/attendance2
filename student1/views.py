from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
def principal(user):
    """Check if the user belongs to the 'Checkers' group."""
    return user.groups.filter(name='principal').exists()

@login_required
@user_passes_test(principal)
def studentlogin(request):
    return render(request,'student1/index1.html') 

