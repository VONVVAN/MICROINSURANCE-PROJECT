from django.core.exceptions import ValidationError
from django import forms
from microinsurance.models import Branch

EMPTY_LIST_ERROR = "You can't have an empty list item"
DUPLICATE_ITEM_ERROR = "You've already got this in your list"

class BranchForm(forms.models.ModelForm):
	class Meta: 
		model = Branch
		fields = [
			'branch_name'
		]

	def clean_name(self):
		branch_name = self.branch_name.strip()
		if branch_name = '':
			raise.forms.ValidationError('Branch Manager must not all be spaces')
		return branch_name	