from django.http.response import HttpResponse
from django.shortcuts import render
from  django.http import HttpResponse 
import random


# Create your views here.

def home(request):
    return render(request,'generator/home.html')
def about(request):

    return render(request,'generator/about.html')

def password(request):

	char = list('abcdefghijklmnopqrsuvwxyz')
	if request.GET.get('uppercase'):
		char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
	if request.GET.get('specialcharacters'):
		char.extend(list('~@#$%^&*+'))
	if request.GET.get('numbers'):
		char.extend(list('1234567890'))




	length=int(request.GET.get('length'))
	thepassword=''
	for i in range(length):
		thepassword +=random.choice(char)

	return render(request,'generator/password.html',{ "password":thepassword })
