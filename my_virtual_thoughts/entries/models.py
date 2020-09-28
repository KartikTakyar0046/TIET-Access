from django.db import models
from django.contrib.auth.models import User		
# Create your models here.

from django.forms import ModelForm
# Batches = (
#     ("24", "COE-24"),
#     ("25", "COE-25"),
#     ("26", "COE-26"),
#     ("27", "COE-27"),
#     ("28", "COE-28"),
# )

class Batch(models.Model):
	# batch_choices= (
 #    	('firstbatch', 'COE-24'),
 #    	('secondbatch', 'COE-25'),
 #    	('thirdbatch', 'COE-26'),
 #    	('fourthbatch', 'COE-27'),
 #    	('fifthbatch', 'COE-28'),
 #    )
	batch=models.CharField(max_length=12)
	def __str__(self):
		return self.batch


class Assignment(models.Model):
	Assignment_Name=models.CharField(max_length=100)
	Date_Published=models.DateTimeField(auto_now_add=True)
	Publishing_Teacher=models.ForeignKey(User, on_delete=models.CASCADE)
	Assignment_Content=models.CharField(max_length=100)
	# firstbatch='COE-24'
	# secondbatch='COE-25'
	# thirdbatch='COE-26'
	# fourthbatch='COE-27'
	# fifthbatch='COE-28'
	
	Batch = models.ForeignKey(Batch,null=True,on_delete=models.SET_NULL)
	class Meta:
		verbose_name_plural="Assignments"

	def __str__(self):
			return f'{self.Assignment_Name}'