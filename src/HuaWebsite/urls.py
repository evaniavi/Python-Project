"""HuaWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView
from personal.views import submit_position, view_positions, view_students, choose_student

from personal.views import (
	home_page_view,
    submit_position,
    view_positions,
    view_students,
    choose_student,
	) 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', home_page_view , name='home'),
    path('submit/', TemplateView.as_view(template_name='submit.html'), name='submit'),
    path('submit/submit_position', submit_position, name='submit_position'),
    path('submit/submit_position/success', TemplateView.as_view(template_name='success_submit.html'), name='success_submit'),
    path('info/', TemplateView.as_view(template_name='info.html'), name='info'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('positions/', view_positions , name='view_positions'),
    path('positions/view_students', view_students, name='view_students'),
    path('positions/choose_student', choose_student, name='choose_student'),
    
]
