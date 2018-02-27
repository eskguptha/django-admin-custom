"""
Django Admin Custom View 
"""
from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import render

def my_custom_view(request, template_name='index.html', context_data={}):
	context_data  = {"msg" : "hello"}
    return render(request, template_name, context_data)

def get_admin_urls(urls):
    def get_urls():
        my_urls = [
            url(r'^your_admin_url/$', admin.site.admin_view(my_custom_view))
        ]
        return my_urls + urls
    return get_urls

admin_urls = get_admin_urls(admin.site.get_urls())
admin.site.get_urls = admin_urls
