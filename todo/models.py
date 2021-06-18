from django.db import models
from django.utils import timezone

# Create your models here.
class Project(models.Model):
    Project_name = models.CharField(max_length=64)
    Project_description = models.CharField(max_length=128)
    Project_isDone = models.BooleanField(default=False)
    Project_deadline = models.DateField(null=True)
    Project_submitDate = models.DateTimeField(default=timezone.now)

class Task(models.Model):
    Task_name = models.CharField(max_length=64)
    Task_description = models.CharField(max_length=128)
    Task_isDone = models.BooleanField(default=False)
    Task_project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    Task_submitDate = models.DateTimeField(default=timezone.now)

