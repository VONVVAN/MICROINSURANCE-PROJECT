from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate

def home_page(request):	
	return render(request, 'index.html')

def log_in(request):
   	return render(request, 'login.html')

def access_granted(request):
	user = authenticate(username='admin', password = 'admin')
	if request.method == 'POST':
		if user is not None:
			print("User is valid")
			return render(request, 'index.html')
		else:
			print("none")
			return render(request, 'login.html')

# Create your views here.
