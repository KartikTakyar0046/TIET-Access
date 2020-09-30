from django.db import models
from django.contrib.auth.models import User		
# Create your models here.
from django.utils.timezone import now

from django.forms import ModelForm

class Assignment(models.Model):
	Assignment_Name=models.CharField(max_length=100)
	Date_Published=models.DateTimeField(auto_now_add=True)
	user=models.ForeignKey(User, on_delete=models.CASCADE, null=True,related_name='assignments')
	upload = models.FileField(upload_to='assignments/', null=True, default="No file uploaded")
	Assignment_Content=models.CharField(max_length=10000)
	Course_Title = models.CharField(max_length=255, default='')
	Course_Code=models.CharField(max_length=8,default='')
	Due_Date = models.DateField(default=now, editable=True)
	Batch = models.CharField(max_length=6,default='')
	class Meta:
		verbose_name_plural="Assignments"

	def __str__(self):
			return f'{self.Assignment_Name}'