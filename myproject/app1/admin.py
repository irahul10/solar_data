from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Student)
admin.site.register(Logindata)

# admin.site.register(student2)
# admin.site.register(login)