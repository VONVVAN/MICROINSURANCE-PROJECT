from django.db import models
import datetime
from django.contrib.auth.models import User

status_choices = (
	('A', 'Active'),
	('I', 'Inactive'),
)


class Branch(models.Model):

	branch_name = models.CharField(
		max_length=100, primary_key = True,
	)
	date_created = models.CharField(default = datetime.datetime.now, max_length = 26)
	status = models.CharField(max_length=7, choices = status_choices, default='Active')

	class Meta:
		verbose_name_plural = "Branches"

	def __str__(self):
		return self.branch_name

class UnderWriter(models.Model):
	
	underwriter_name = models.CharField(
		max_length = 100,
	)
	underwriter_address = models.TextField()
	
	underwriter_contact_person = models.CharField(
		max_length = 100,
	)
	underwriter_contact_no = models.CharField(
		max_length = 11,
	)
	date_created = models.CharField(default = datetime.datetime.now, max_length = 26)
	status = models.CharField(max_length=7, choices = status_choices, default='Active')

	def __str__(self):
		return self.underwriter_name

class MicroinsuranceType(models.Model):

	Microinsurance_Type_Name = models.CharField(
		max_length = 100,
	)
	date_created = models.CharField(default = datetime.datetime.now, max_length = 26)
	status = models.CharField(max_length=7, choices = status_choices, default='Active')

	def __str__(self):
		return self.Microinsurance_Type_Name

class MicroinsuranceOffered(models.Model):

	Microinsurance_Code = models.CharField(
		max_length = 10,
	)
	Microinsurance_Name = models.CharField(
		max_length = 100,
	)
	Microinsurance_Description = models.TextField(
		max_length = 200,
	)

	Microinsurance_Type_Name = models.ForeignKey(MicroinsuranceType)
	underwriter_name = models.ForeignKey(UnderWriter)
	Microinsurance_Base_Price = models.CharField(
		max_length = 100, default = 0,
	)
	Microinsurance_Price = models. CharField(
		max_length = 100, default = 0,
	)

	Minimum_Age = models.IntegerField(default=0)
	Maximum_Age = models.IntegerField(default=0)

	Limitation_Per_Person = models.IntegerField(default=0)
	Days_Of_Validity = models.IntegerField(default=0)
	
	Date_Effective_Start = models.DateTimeField(default = datetime.datetime.now())
	Date_Effective_End = models.DateTimeField(default = datetime.datetime.now())

	date_created = models.CharField(default = datetime.datetime.now, max_length = 26)
	status = models.CharField(max_length=7, choices = status_choices, default='Active')

	class Meta:
		verbose_name_plural = 'Microinsurance Offered'

	def __str__(self):
		return self.Mnsurance_Name


class UserType(models.Model):

	User_Type_Name = models.CharField(max_length=100,)
	date_created = models.CharField(default = datetime.datetime.now, max_length = 26)
	status = models.CharField(max_length=7, choices = status_choices, default='Active')

	def __str__(self):
		return self.User_Type_Name

class UserAccess(models.Model):

	user = models.OneToOneField(User)
	User_Type_Name = models.ForeignKey(UserType)
	date_created = models.CharField(default = datetime.datetime.now, max_length = 26)
	status = models.CharField(max_length=7, choices = status_choices)

	class Meta:
		verbose_name_plural='User Access'

	def __str__(self):
		return self.user.first_name




