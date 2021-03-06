"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from microinsurance.views import home_page, log_in, access_granted, save_insurance, front_liner, old_applicant, search_applicant,  add_new_insurance_registered_applicant

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'microinsurance.views.home_page', name='home'),
    url(r'^login/', 'microinsurance.views.log_in', name ='login'),
 	#url(r'^authenticate/', 'microinsurance.views.access_granted'),
    url(r'^validation', 'microinsurance.views.access_granted', name ='validation'),
    url(r'^frontliner', 'microinsurance.views.front_liner', name ='frontliner'),
    url(r'^save/', 'microinsurance.views.save_insurance', name ='save'),
    url(r'^searchapplicant', 'microinsurance.views.search_applicant', name ='save'),
    url(r'^oldapplicant', 'microinsurance.views.old_applicant', name ='oldapplicant'),
    url(r'^addinsurance', 'microinsurance.views.add_new_insurance_registered_applicant', name ='addinsurance'),
]
