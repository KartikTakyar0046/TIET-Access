from django.contrib import admin

# Register your models here.
from .models import Batch, Assignment

admin.site.register(Batch)	 
admin.site.register(Assignment)	 