
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
STUDENT=1
TEACHER=2
choice=((STUDENT,'Student'),
			(TEACHER,'Teacher'),
)
COE27=27
COE28=28
COE29=29
COE30=30
BATCH_CHOICE=((COE27,'COE-27'),
				(COE28,'COE-28'),
				(COE29,'COE-29'),
				(COE30,'COE-30'),
)
class Batch(models.Model):
	batch=models.PositiveSmallIntegerField(choices=BATCH_CHOICE, null=True,blank=True,unique=True)
	def __str__(self):
		return f'{self.batch}'
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.PositiveSmallIntegerField(choices=choice, null=True, blank=True)
    batch=models.ForeignKey(Batch, on_delete=models.CASCADE, null=True)
    def __str__(self):
    	return f'{self.user.username}'