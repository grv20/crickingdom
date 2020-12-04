from django.contrib import admin
from .models import Subject, Teacher, Student

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Subject)
# Register your models here.
