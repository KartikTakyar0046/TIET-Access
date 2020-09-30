from django.contrib import admin

# Register your models here.
from .models import Profile,Batch
admin.site.register(Profile)

admin.site.register(Batch)
