from django.contrib import admin
from .models import Student, Teacher, Science_Group

admin.site.register([Student, Teacher, Science_Group])