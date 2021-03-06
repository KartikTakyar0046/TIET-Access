"""my_virtual_thoughts URL Configuration

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

from . import views

from django.contrib.auth import views as auth_views
from .views import dashboard,assign,mybatch,stu_dashboard,assign_stu
from entries.views import tt
from django.urls import path
urlpatterns = [
    # path('register/',views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="logout.html"), name="logout"),
    path('dashboard/',dashboard, name='dashboard'),
    path('dashboard/assignments/',assign,name='assign'),
    path('dashboard/mybatch/',mybatch, name='mybatch'),
    path('stu_dashboard/',stu_dashboard, name='stu_dashboard'),
    path('stu_dashboard/assignments',assign_stu,name='assign_stu'),
    path('stu_dashboard/timetable',tt,name='timetable'),
 
]
