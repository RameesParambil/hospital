from django.contrib import admin
from .models import Doctors
from .models import Departments
# Register your models here.
admin.site.register(Doctors)
admin.site.register(Departments)