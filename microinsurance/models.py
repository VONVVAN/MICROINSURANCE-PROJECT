from django.db import models
import datetime
from django.contrib.auth.models import User
from django.core import validators

status_choices = (
	('A', 'Active'),
	('I', 'Inactive'),
)

class Branch(models.Model):

	branch_name = models.CharField(
		max_length=100, unique = True,
		validators=[
            validators.RegexValidator(r'^[\s\w.-]+$',
                                      ('Enter a valid Branch Name. '
                                        'This value may contain only letters, numbers '
                                        'and /./-/_ characters.'), 'invalid'),
        ],
	)
	date_created = models.CharField(default = datetime.datetime.now, max_length = 26)
	status = models.CharField(max_length=7, choices = status_choices, default='Active')
	class Meta:
		verbose_name_plural = "Branches"

	def __str__(self):
		return self.branch_name

class UnderWriter(models.Model):
	
	underwriter_name = models.CharField(
		max_length = 100, unique = True,
		validators=[
            validators.RegexValidator(r'^[^\d]+$',
                                      ('Enter a valid UnderWriter Name. '
                                        'This value may contain only letters, numbers '
                                        'and ./-/_ characters.'), 'invalid'),
        ],
	)
	underwriter_address = models.TextField(
		max_length = 100,
		validators=[
            validators.RegexValidator(r'^[\s\w.-]+$',
                                      ('Enter a valid Address. '
                                        'This value may contain only letters, numbers '
                                        'and ./-/_ characters.'), 'invalid'),
        ],
	)
	
	underwriter_contact_person = models.CharField(
		max_length = 100,
		validators=[
            validators.RegexValidator(r'^[^\d]+$',
                                      ('Enter a valid Name. '
                                        'This value may contain only letters'), 'invalid'),
        ],
	)
	underwriter_contact_no = models.CharField(
		max_length = 11, unique = True,
		validators=[
            validators.RegexValidator(r'^[0-9]+$',
                                      ('Enter a valid contact no. '
                                        'only accepts numbers'), 'invalid'),
        ],
	)
	date_created = models.CharField(default = datetime.datetime.now, max_length = 26)
	status = models.CharField(max_length=7, choices = status_choices, default='Active')

	def __str__(self):
		return self.underwriter_name

class MicroinsuranceType(models.Model):

	Microinsurance_Type_Name = models.CharField(
		max_length = 100, unique = True,
		validators=[
            validators.RegexValidator(r'^[^\d]+$',
                                      ('Enter a valid Name. '
                                        'This value may contain only letters'), 'invalid'),
        ],
	)

	date_created = models.CharField(default = datetime.datetime.now, max_length = 26)
	status = models.CharField(max_length=7, choices = status_choices, default='Active')

	def __str__(self):
		return self.Microinsurance_Type_Name

class MicroinsuranceOffered(models.Model):

	Microinsurance_Code = models.CharField(
		validators=[
            validators.RegexValidator(r'^[\d\w-]+$',
                                      ('Enter a valid Code. '
                                        'This value may contain numbers, letters and "-" character'), 'invalid'),
        ],
		max_length = 10, unique = True,
	)
	Microinsurance_Name = models.CharField(
		max_length = 100, unique = True, default='',
		validators=[
            validators.RegexValidator(r'^[^\d]+$',
                                      ('Enter a valid Name. '
                                        'This value may contain only letters'), 'invalid'),
        ],
	)
	Microinsurance_Description = models.TextField(
		max_length = 200,
		validators=[
            validators.RegexValidator(r'^[\s\d\w-]+$',
                                      ('Enter a valid Name. '
                                        'This value may contain only letters, numbers and ".-" characters'), 'invalid'),
        ],
	)

	Microinsurance_Type_Name = models.ForeignKey(MicroinsuranceType)
	underwriter_name = models.ForeignKey(UnderWriter)
	Microinsurance_Base_Price = models.CharField(
		max_length = 100, default = 0,
	)
	Microinsurance_Price = models. CharField(
		max_length = 100, default = 0,
	)

	Minimum_Age = models.CharField(
		max_length = 3, default=0,
		validators=[
            validators.RegexValidator(r'^[0-9]+$',
                                      ('Enter a valid Age. '
                                        'This value may contain only numbers'), 'invalid'),
        ],
	)
	Maximum_Age = models.CharField(
		max_length = 3, default=0,
		validators=[
            validators.RegexValidator(r'^[0-9]+$',
                                      ('Enter a valid Age. '
                                        'This value may contain only numbers'), 'invalid'),
        ],
	)

	Limitation_Per_Person = models.CharField(
		max_length = 2, default=0,
		validators=[
            validators.RegexValidator(r'^[0-9]+$',
                                      ('Enter a valid Numebr. '
                                        'This value may contain only numbers'), 'invalid'),
        ],
	)
	
	Days_Of_Validity = models.CharField(
		max_length = 3, default=0,
		validators=[
            validators.RegexValidator(r'^[0-9]+$',
                                      ('Enter a valid Number. '
                                        'This value may contain only numbers'), 'invalid'),
        ],

	)
	
	Date_Effective_Start = models.DateTimeField(default = datetime.datetime.now())
	Date_Effective_End = models.DateTimeField(default = datetime.datetime.now())

	date_created = models.CharField(default = datetime.datetime.now, max_length = 26)
	status = models.CharField(max_length=7, choices = status_choices, default='Active')

	class Meta:
		verbose_name_plural = 'Microinsurance Offered'

	def __str__(self):
		return self.Microinsurance_Name


class UserType(models.Model):

	User_Type_Name = models.CharField(max_length=100, unique = True,
		validators=[
            validators.RegexValidator(r'^[^\d]+$',
                                      ('Enter a valid Name. '
                                        'This value may contain only letters'), 'invalid'),
        ],
	)
	
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

class Applicant(models.Model):

	first_name = models.CharField(
		max_length = 100,  
	)

	last_name = models.CharField(
		max_length = 100,
	)
	middle_name = models.CharField(
		max_length = 100,
	)
	suffix = models.CharField(
		max_length = 5,
	)
	birthdate = models.CharField(
		max_length = 100,
	)
	contact_no =models.CharField(
		max_length = 11, unique = True,
	)
	address = models.CharField(
		max_length = 100,
	)
	microinsurance= models.CharField(
		max_length = 100,
	)
	quantity = models.CharField(
		max_length = 3,
	)
	policy_no = models.CharField(
		max_length = 20, unique = True,
	)

	def __str__(self):
		return self.last_name
