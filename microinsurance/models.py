from django.db import models

class Branch(models.Model):

	branch_name = models.CharField(
		max_length=225, primary_key = True,
	)

	class Meta:
		verbose_name_plural = "branches"

	def __str__(self):
		return self.branch_name



class UserType(models.Model):

	user_type = models.CharField(
		max_length = 225, unique = True, 
	)

	def __str__(self):
		return self.user_type

class SystemUser(models.Model):

	first_name = models.CharField(
		max_length = 225,
	)
	last_name = models.CharField(
		max_length = 225,
	)
	middle_name = models.CharField(
		max_length = 225, blank = True,
	)
	contact_no = models.CharField(
		max_length = 225,
	)

	user_type = models.ForeignKey(UserType, max_length = 200)

	branch_name = models.ForeignKey(Branch, max_length = 200)

	def __str__(self):
		return '%s %s' % (self.first_name, self.last_name)




