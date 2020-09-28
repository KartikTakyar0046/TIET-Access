from django import forms
from .models import Assignment,Batch
class AssignmentForm(forms.ModelForm):
	class Meta:
		model=Assignment
		fields=['Batch', 'Assignment_Name', 'Assignment_Content']	