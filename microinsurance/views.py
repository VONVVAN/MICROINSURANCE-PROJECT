from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from microinsurance.models import MicroinsuranceOffered, Branch, Applicant, UserType, UserAccess
from django.contrib.auth.models import User

def home_page(request):	
	return render(request, 'index.html')

def log_in(request):
   	return render(request, 'login.html')

def access_granted(request):
	usern = request.POST.get("username", "")
	userp = request.POST.get("password", "")
	user = authenticate(username=usern, password = userp)
	#usertype  =  UserType(User_Type_Name='Front Liner')
	#queryset = MicroinsuranceOffered.objects.get(Microinsurance_Name)
	category_list = MicroinsuranceOffered.objects.order_by('Microinsurance_Name')
	if user is not None:
		return render(request, 'transaction.html', {'usern': usern, 'category_list': category_list})
	else:
		print("none")
		return render(request, 'login.html')

def save_insurance(request):
	firstname = request.POST.get('firstname', '')
	lastname = request.POST.get('lastname', '')
	middlename = request.POST.get('middlename', '')
	suffix = request.POST.get('suffix', '')
	birthdate = request.POST.get('month', '')
	contactno = request.POST.get('contactno', '')
	address = request.POST.get('address', '')
	microinsurance = request.POST.get('microinsurance', '')
	quantity = request.POST.get('quantity', '')
	policyno = request.POST.get('policyno', '')
	category_list = MicroinsuranceOffered.objects.order_by('Microinsurance_Name')
	if firstname.strip() == '':
		return render(request, 'transaction.html', {'category_list': category_list})
	else:
		insurance = Applicant(first_name=firstname, last_name=lastname, middle_name =middlename, suffix = suffix, birthdate = birthdate, contact_no=contactno, address=address, Microinsurance_Name = microinsurance, quantity=quantity, policy_no=policyno )
		insurance.save()
		return render(request, 'transaction.html', {'category_list': category_list})
# Create your views here.
