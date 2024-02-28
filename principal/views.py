from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def principallogin(request):
    return render(request,'principal1/index5.html') 