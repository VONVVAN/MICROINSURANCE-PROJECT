from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout

def home_page(request):	
	return render(request, 'index.html')

def logout_view(request):
   	logout(request, 'index.html')
    # Redirect to a 

# Create your views here.
