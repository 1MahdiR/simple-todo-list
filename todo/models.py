from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    isDone = models.BooleanField(default=False)
    deadline = models.DateField(null=True)
    submitDate = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Task(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    doer = models.CharField(max_length=64)
    isDone = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    submitDate = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, default=project, on_delete=models.CASCADE)

