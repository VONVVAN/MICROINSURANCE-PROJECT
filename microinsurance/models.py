from django.db import models
import datetime

class Branch(models.Model):

	branch_name = models.CharField(
		max_length=225, primary_key = True,
	)

	class Meta:
		verbose_name_plural = "branches"

	def __str__(self):
		return self.branch_name


class UnderWriter(models.Model):
	
	underwriter_name = models.CharField(
		max_length = 225,
	)
	underwriter_address = models.TextField()
	
	underwriter_contact_person = models.CharField(
		max_length = 225,
	)
	underwriter_contact_no = models.CharField(
		max_length = 225,
	)

	def __str__(self):
		return self.underwriter_name

class InsuranceType(models.Model):

	Insurance_Type_Name = models.CharField(
		max_length = 225,
	)

	def __str__(self):
		return self.Insurance_Type_Name

class Insurance(models.Model):

	Insurance_Name = models.CharField(
		max_length = 225,
	)

	Insurance_Type_Name = models.ForeignKey(InsuranceType)
	underwriter_name = models.ForeignKey(UnderWriter)
	Insurance_Base_Price = models.CharField(
		max_length = 225, default = 0,
	)
	Insurance_Price = models. CharField(
		max_length = 225, default = 0,
	)

	Minimum_Age = models.IntegerField(default=0)
	Maximum_Age = models.IntegerField(default=0)

	Limitation_Per_Person = models.IntegerField(default=0)
	Days_Of_Validity = models.IntegerField(default=0)
	
	Date_Effective_Start = models.DateTimeField(default = datetime.datetime.now())
	Date_Effective_End = models.DateTimeField(default = datetime.datetime.now())

class Discount(models.Model):

	Discount_Name = models.CharField(max_length=225,)
	Insurance_Name = models.ForeignKey(Insurance)
	Percentage = models.IntegerField()
	Date_Start = models.DateTimeField(default= datetime.datetime.now)
	Date_End = models.DateTimeField(default=datetime.datetime.now)









#class UserType(models.Model):

#	user_type = models.CharField(
#		max_length = 225, unique = True, 
#	)

#	def __str__(self):
#		return self.user_type

#class SystemUser(models.Model):

#	first_name = models.CharField(
#		max_length = 225,
#	)
#	last_name = models.CharField(
#		max_length = 225,
#	)
#	middle_name = models.CharField(
#		max_length = 225, blank = True,
#	)
#	contact_no = models.CharField(
#		max_length = 225,
#	)

#	user_type = models.ForeignKey(UserType, max_length = 200)
#
#	branch_name = models.ForeignKey(Branch, max_length = 200)

#	def __str__(self):
#		return '%s %s' % (self.first_name, self.last_name)




