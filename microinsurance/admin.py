from django.contrib import admin
from microinsurance.models import Branch, UserType, SystemUser
from django.contrib.auth.models import Group

admin.site.register(Branch)
admin.site.register(UserType)
admin.site.register(SystemUser)
admin.site.unregister(Group)
