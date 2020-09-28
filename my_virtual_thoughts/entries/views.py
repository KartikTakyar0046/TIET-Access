from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Assignment
# # Create your views here.
from django.views.generic import ListView,DetailView ,CreateView
from .forms import AssignmentForm

class Homepage(ListView):
	model=Assignment
	template_name='index.html'
	context_object_name="assignment_entries"
	ordering=['-Date_Published']
	paginate_by=3

class EntryView(DetailView):
	model=Assignment
	template_name='detailed.html'

def CreatePost(request):
	form=AssignmentForm(request.POST or None)
	if form.is_valid():
		form.save()
	context={}
	context['form']=form
	return render(request, 'create_post.html',context)

