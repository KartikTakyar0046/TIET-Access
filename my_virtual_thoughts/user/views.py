from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from entries.forms import AssignmentForm
from entries.models import Assignment
from .models import Profile
# from . forms import RegistrationForm
# Create your views here.
# def register(request):
# 	if request.method=="POST":
# 		form=RegistrationForm(request.POST)
# # 		if form.is_valid():
# # 			form.save()
# # 	else:
# # 		form=RegistrationForm()
# # 	context={'form': form}
# # 	return render(request, 'register.html', context)
@login_required
def dashboard(request):
	logged_in_user=request.user
	assignments=Assignment.objects.filter(user=logged_in_user)
	users=Profile.objects.all()
	if logged_in_user.profile.role==2:
		context={'assignments':assignments,'users':users}	
		return render(request, 'teacher_dashboard.html', context=context)
def assign(request):
	logged_in_user=request.user
	assignments=Assignment.objects.filter(user=logged_in_user)
	context={'assignments':assignments}
	return render(request,'assign.html',context=context)


def assign_stu(request):
	assignment_entries=Assignment.objects.all()
	context={'assignment_entries':assignment_entries}
	return render(request,'assign_stu.html',context=context)


def stu_dashboard(request):
	logged_in_user=request.user
	stu=request.user.profile
	assignments=Assignment.objects.filter(user=logged_in_user)
	if logged_in_user.profile.role==1:
		context={'assignments':assignments}
		return render(request,'student_dashboard.html', context=context)


def mybatch(request):
	logged_in_user=request.user
	users=Profile.objects.all()
	context={'users':users}
	return render(request, 'mybatch.html', context=context)
