from django.db import models
from django.utils import timezone

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    isDone = models.BooleanField(default=False)
    deadline = models.DateField(null=True)
    submitDate = models.DateTimeField(default=timezone.now)

class Task(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    isDone = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    submitDate = models.DateTimeField(default=timezone.now)

