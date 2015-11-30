from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from microinsurance.models import UserType
from django.contrib.auth.models import User

def home_page(request):	
	return render(request, 'index.html')

def log_in(request):
   	return render(request, 'login.html')

def access_granted(request):
	usern = request.POST.get("username", "")
	userp = request.POST.get("password", "")
	#userf = User.objects.get(id=user_id).username
	user = authenticate(username=usern, password = userp)
	#userf = User.objects.get('first name')
	usertype  =  UserType(User_Type_Name='Front Liner')
	if user is not None:
		if usertype is not None:
			return render(request, 'transaction.html', {'usern': usern})
		else:
			return render(request, 'index.html')
	else:
		print("none")
		return render(request, 'login.html')


# Create your views here.
