from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from microinsurance.models import MicroinsuranceOffered, Branch, Transaction, Applicant, UserType, BranchAccess
from django.contrib.auth.models import User
from django.core import validators
from microinsurance.forms import LoginForm
from django.http import HttpResponseRedirect
import datetime

loginerror = 'Incorrect Username or Password'
requiredfields = 'Please fill up required fields'
contacterror = 'Contact Number must be unique !'	
error = ''
required = 'required'
limitation = 'quantity must not be greate than the limit !'
brancherror = 'No such branch'
applicanterror = 'Applicant does not exist!'
ageerror= 'Applicant must satisfy the age requirement!'

def home_page(request):	
	return render(request, 'index.html')

def log_in(request):
	formlog = LoginForm(request.POST or None)	
	return render(request, 'login.html', {'formlog': formlog })
   	#return render(request, 'login.html', {'formlog': formlog })

def access_granted(request):
	usern = request.POST.get("username", "")
	userp = request.POST.get("password", "")
	formlog = LoginForm(request.POST or None)
	user = authenticate(username=usern, password = userp)
	get_user = User.objects.select_related().filter(username = usern)
	for userc in get_user:
		print(userc.id)
		userid = userc.id
		name = userc.first_name
	get_usertype = BranchAccess.objects.select_related().filter(user = userid)
	for types in get_usertype:
		status = str (types.status)
		branch_name = str (types.branch_name)
		finalusertype = str (types.User_Type_Name)
		print(status)
	category_list = MicroinsuranceOffered.objects.order_by('Microinsurance_Name')
	request.session['user'] = name
	request.session['branch'] = branch_name
	if user is not None:
		if status =='A':
			if finalusertype == 'Branch Manager':
				return HttpResponseRedirect('/frontliner')
			else:
				return HttpResponseRedirect('/')
		else:
			return render(request, 'login.html', {'formlog': formlog })
	else:
		return render(request, 'login.html', {'formlog': formlog })

def front_liner(request):
	name = request.session['user']
	branchname = request.session['branch']
	category_list = MicroinsuranceOffered.objects.order_by('Microinsurance_Name')
	return render(request, 'transaction.html', {'category_list': category_list, 'name': name, 'branchname' :branchname })


def old_applicant(request):
	ctr = ''
	lastname=''
	firstname=''
	contact =''
	customerdata = []
	customerrawdata =''
	all_applicants = Applicant.objects.all()
	category_list = MicroinsuranceOffered.objects.order_by('Microinsurance_Name')
	print(all_applicants)
	for data in all_applicants:
		ctr = ctr +str('i')
		customerrawdata = str(data.first_name) + ' ' + str(data.last_name) + ' ' + str(data.contact_no)   
		customerdata.append(customerrawdata)
	name = request.session['user']
	branchname = request.session['branch']
	return render(request, 'oldapplicant.html', {'name': name, 'branchname': branchname, 'customerdata': customerdata, 'category_list': category_list })

def search_applicant(request):
	firstname =''
	last_name =''
	contact = request.POST.get('searchcontact', '')
	name = request.session['user']
	branchname = request.session['branch']
	category_list = MicroinsuranceOffered.objects.order_by('Microinsurance_Name')
	print(contact)
	get_applicant = Applicant.objects.select_related().filter(contact_no = contact)
	for data in get_applicant:
		firstname = data.first_name
		lastname = data.last_name
		contactno = data.contact_no
	if firstname != '':
		print(firstname)
		return render(request, 'oldapplicant.html', {'lastname': lastname, 'contactno':contactno, 'firstname': firstname, 'category_list':category_list, 'branchname': branchname, 'name': name })
	else:
		error = applicanterror
		return render(request, 'oldapplicant.html', {'error': error, 'category_list':category_list, 'branchname': branchname, 'name': name})

def add_new_insurance_registered_applicant(request):
	name = request.session['user']
	branchname = request.session['branch']	
	contactno = request.POST.get('contactno', '')
	get_applicant = Transaction.objects.select_related().filter(contact_no = contact)
	category_list = MicroinsuranceOffered.objects.order_by('Microinsurance_Name')		
	return render(request, 'oldapplicant.html', {'name': name, 'branchname': branchname, 'category_list': category_list })

def save_insurance(request):
	failmicro =''
	failcontact =''
	price = ''
	agelimit =0
	birthdate =''
	agepass ='not'
	now = datetime.datetime.now()
	firstname = request.POST.get('firstname', '')
	lastname = request.POST.get('lastname', '')
	middlename = request.POST.get('middlename', '')
	suffix = request.POST.get('suffix', '')
	birthdate = request.POST.get('birthday', '')
	contactno = request.POST.get('contactno', '')
	address = request.POST.get('address', '')
	microinsurance = request.POST.get('microinsurance', '')
	quantity = request.POST.get('quantity', '')
	policyno = request.POST.get('policyno', '')
	category_list = MicroinsuranceOffered.objects.order_by('Microinsurance_Name')
	name = request.session['user']
	branchname = request.session['branch']
	all_microinsurance = MicroinsuranceOffered.objects.all()
	all_contacts = Applicant.objects.all()
	yearv  = int(birthdate[6:10])
	monthv = int(birthdate[:2])
	dayv = int(birthdate[3:5])
	#print (validbday)
	yearf = int(now.year) - yearv
	monthnow = int(now.month)
	daynow = int(now.day)
	print(yearf)
	print(birthdate)
	for micro in all_microinsurance:
		if microinsurance == micro.Microinsurance_Name:
			failmicro = micro.Microinsurance_Name
		else:
			failmicro = ''
	get_limit = MicroinsuranceOffered.objects.select_related().filter(Microinsurance_Name = microinsurance)
	for items in get_limit:
		microlimit = items.Limitation_Per_Person
		price = (items.Microinsurance_Price)
		agelimit = int(items.Minimum_Age)
		print(microlimit)
	for cont in all_contacts:
		print(cont.contact_no)
		if cont.contact_no == contactno:
			failcontact = cont.contact_no
		else:
			failcontact = ''

	if yearf < agelimit:
		agepass = 'not'		
	elif yearf == agelimit:
		if monthv > monthnow:
			agepass = 'not'					
		elif monthv == monthnow:
			if dayv > daynow:
				agepass = 'not'						
			else:
				agepass = 'pass' 
	elif yearf > agelimit:
		agepass = 'pass'

	dateyear = str(now.year)
	datemonth = str(now.month)
	dateday = str(now.day)
	if datemonth == '1':
		datemonth = '01'
	elif datemonth == '2':
		datemonth = '02'
	elif datemonth == '3':
		datemonth = '03'
	elif datemonth == '4':
		datemonth = '04'
	elif datemonth == '5':
		datemonth = '05'
	elif datemonth == '6':
		datemonth = '06'
	elif datemonth == '7':
		datemonth = '07'
	elif datemonth == '8':
		datemonth = '08'
	elif datemonth == '9':
		datemonth = '09'
	if dateday == '1':
		dateday = '01'
	elif dateday == '2':
		dateday = '02'
	elif dateday == '3':
		dateday = '03'
	elif dateday == '4':
		dateday = '04'
	elif dateday == '5':
		dateday = '05'
	elif ddateday == '6':
		dateday = '06'
	elif dateday == '7':
		dateday = '07'
	elif dateday == '8':
		dateday = '08'
	elif datedayh == '9':
		dateday = '09'
	datefinal = datemonth+"/"+dateday+"/"+dateyear
	if firstname.strip() == '' or lastname.strip()== '' or contactno.strip()=='' or address.strip()=='' or quantity.strip()=='' or policyno.strip()=='':
		error = requiredfields
		return render(request, 'transaction.html', {'category_list': category_list, 'error': error, 'name': name, 'branchname': branchname, 'required': required })
	
	elif failcontact == contactno:
		error = contacterror
		return render(request, 'transaction.html', {'category_list': category_list, 'error': error, 'name': name, 'branchname': branchname })	
	elif microlimit < quantity:
		error = limitation
		return render(request, 'transaction.html', {'category_list': category_list, 'error': error, 'name': name, 'branchname': branchname })	
	elif agepass == 'not':
		error = ageerror
		return render(request, 'transaction.html', {'category_list': category_list, 'error': error, 'name': name, 'branchname': branchname })	
	else:	
		print(birthdate)
		trans = Transaction(transfname=firstname, translname = lastname, transcontactno = contactno, transmicro = microinsurance, amount_paid = price, quantity = quantity, policyno = policyno, transdate = datefinal )
		insurance = Applicant(first_name=firstname, last_name=lastname, middle_name =middlename, suffix = suffix, birthdate = birthdate, contact_no=contactno, address=address)
		print (trans)
		insurance.save()
		trans.save()
		return render(request, 'transaction.html', {'category_list': category_list, 'branchname': branchname, 'name': name })

