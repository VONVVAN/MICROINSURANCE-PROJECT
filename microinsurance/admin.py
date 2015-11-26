from django.contrib import admin
from microinsurance.models import Branch, UnderWriter, InsuranceType, Insurance, Discount
from django.contrib.auth.models import Group

admin.site.register(Branch)
admin.site.register(UnderWriter)
admin.site.register(InsuranceType)
admin.site.register(Insurance)
admin.site.register(Discount)
admin.site.unregister(Group)
