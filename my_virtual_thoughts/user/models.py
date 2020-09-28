
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
STUDENT=1
TEACHER=2
choice=((STUDENT,'Student'),
			(TEACHER,'Teacher'),
)
class Profile(models.Model):
	
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.PositiveSmallIntegerField(choices=choice, null=True, blank=True)
    def __str__(self):
    	return f'{self.user.username} Profile'