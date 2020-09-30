from django import forms
from .models import Assignment
class AssignmentForm(forms.ModelForm):
	
	class Meta:
		model=Assignment
		fields=['Course_Title','Course_Code','Assignment_Name', 'Assignment_Content','Due_Date','upload','Batch']	