
from django import forms

from .models import Task, Project

class AddTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('name', 'description', 'project')

