from django.contrib import admin

# Register your models here.
from .models import Question
#from this directory get the models and import
#the class question from the models (import
#the question model). register that model
#inside of the admin

admin.site.register(Question)
