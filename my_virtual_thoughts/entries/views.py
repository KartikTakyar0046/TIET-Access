from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Assignment
# # Create your views here.
from django.views.generic import ListView,DetailView ,CreateView
from .forms import AssignmentForm
from django.urls import reverse

class Homepage(ListView):
	model=Assignment
	template_name='assign_stu.html'
	context_object_name="assignment_entries"
	ordering=['-Date_Published']
	paginate_by=3


# def stu_ass(request):
# 	assignment_entries=Assignment.objects.all()
# 	context={'assignment_entries':assignment_entries}
# 	return render(request, 'assign_stu.html', context=context)

class EntryView(DetailView):
	model=Assignment
	template_name='detailed.html'


def CreatePost(request):
	form=AssignmentForm(request.POST)
	if not request.user.is_authenticated:
		return render(request, 'index.html')
	else:
		if request.method=='POST':
			if form.is_valid():
				ass=form.save(commit=False)
				ass.user_id=request.user.id
				ass.save()
				new_data = Assignment.objects.last()
			context={'ass':form}
			return render(request, 'index.html',context)
		else:
			form=AssignmentForm(request.POST)
		return render(request, 'create_post.html', {'form':form})
