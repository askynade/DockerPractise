from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import random
def home(request):
    return render(request,'home.html')

def password(request):
    allCh = list("abcdefghijklmnopqrstuvwxyz")
    
    if request.GET.get('uppercase'):
        allCh.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    if request.GET.get('special'):
        allCh.extend(list("!@#$%^&*()"))


    if request.GET.get('number'):
        allCh.extend(list("0123456789"))

    
    length = int(request.GET.get('length'),12)
    
    password =""
    
    for i in range(length):
        password+=random.choice(allCh)
    
    
    return render(request,'password.html',{"password":password})
