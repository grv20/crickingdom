from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
# Create your models here.

User = settings.AUTH_USER_MODEL

class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject, null=True, blank=True)

    # def user_did_save(sender, instance, created, *args, **kwargs):
    #     if created:
    #         Teacher.objects.get_or_create(user=instance)

    # post_save.connect(user_did_save, sender=User)

    def __str__(self):
        return self.user.username

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teachers = models.ManyToManyField(Teacher, null=True, blank=True)

    def __str__(self):
        return self.user.username