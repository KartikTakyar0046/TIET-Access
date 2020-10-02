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
''' These URL Patterens are used to link urls to views, it will be useful if you create the views first and the linke the urls to the views. 

'''
from django.urls import path
from django.conf.urls import url
from .views import Homepage,CreatePost,EntryView
urlpatterns = [
	path('', Homepage,name="Homepage"),
	path('assignment_detail' , EntryView.as_view(), name="assignment-detail"),
	path('create_assignment/',CreatePost,name='create-assignment'),
   # path('/user/stu_dashboard/assignments', stu_ass,name="stu_ass"),
]
