from django.contrib import admin
from microinsurance.models import Branch, UnderWriter, MicroinsuranceType, MicroinsuranceOffered, UserType, BranchAccess, Applicant, Transaction
from django.contrib.auth.models import Group, User
from django.contrib.admin.actions import delete_selected

def make_inactive(modeladmin, request, queryset):
    queryset.update(status='I')
make_inactive.short_description = "Delete Selected Item"

def make_active(modeladmin, request, queryset):
    queryset.update(status='A')
make_active.short_description = "Mark selected choice as Active"

class UserTypeAdmin(admin.ModelAdmin):
	list_display = ['User_Type_Name', 'status']
	ordering = ['User_Type_Name']
	actions = [make_inactive]

class BranchAdmin(admin.ModelAdmin):
	list_display = ['branch_name', 'status']
	ordering = ['branch_name']
	actions = [make_inactive]

class UnderWriterAdmin(admin.ModelAdmin):
	list_display = ['underwriter_name', 'status']
	ordering = ['underwriter_name']
	actions = [make_inactive]

class MicroinsuranceTypeAdmin(admin.ModelAdmin):
	list_display = ['Microinsurance_Type_Name', 'status']
	ordering = ['Microinsurance_Type_Name']
	actions = [make_inactive]

class MicroinsuranceOfferedAdmin(admin.ModelAdmin):
	list_display = ['Microinsurance_Name', 'status']
	ordering = ['Microinsurance_Name']
	actions = [make_inactive]

class BranchAccessAdmin(admin.ModelAdmin):
	list_display = ['user', 'status']
	ordering = ['user']
	actions = [make_inactive]

class DeleteNotAllowedModelAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False


delete_selected.short_description = ''

admin.site.register(Branch, BranchAdmin)
admin.site.register(UnderWriter, UnderWriterAdmin )
admin.site.register(MicroinsuranceType, MicroinsuranceTypeAdmin)
admin.site.register(MicroinsuranceOffered, MicroinsuranceOfferedAdmin)
admin.site.unregister(Group)
admin.site.register(Applicant)
admin.site.register(BranchAccess, BranchAccessAdmin)
admin.site.register(UserType, UserTypeAdmin)