from django.core.exceptions import ValidationError
from django import forms
from microinsurance.models import Branch, Applicant
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

EMPTY_LIST_ERROR = "You can't have an empty list item"
DUPLICATE_ITEM_ERROR = "You've already got this in your list"

class LoginForm(forms.ModelForm):

	username = forms.CharField( widget=forms.TextInput(attrs={'class ':'form-control input-lg','placeholder' : 'Username'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class ':'form-control input-lg','placeholder' : 'Password'}))

	class Meta: 
		model = User
		fields = ['username','password']

	def clean(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		if not user or not user.is_active:
			raise forms.ValidationError("Invalid Username or Password")
		return self.cleaned_data

	def login(self,request):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		return user

