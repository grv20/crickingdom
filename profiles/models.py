from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject, related_name='teachers', null=True, blank=True)

    def __str__(self):
        return self.user.username

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teachers = models.ManyToManyField(Teacher, related_name='students', null=True, blank=True)

    def __str__(self):
        return self.user.username