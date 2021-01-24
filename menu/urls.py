#coding:utf-8
from django.urls import path, include
from . import views

from django.views.generic import TemplateView

app_name = 'menu'


urlpatterns = [
	path('', TemplateView.as_view(template_name = 'menu/home.html'), name='home'),
	
	
	

		  
];