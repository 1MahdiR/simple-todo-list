
from django import forms
from django.utils import timezone

from .models import Task, Project

class AddTaskForm(forms.Form):

    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    doer = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    PROJECTS = [ (item.pk,item.name) for item in Project.objects.all() ]
    PROJECTS.append((0, "No project"))
    project = forms.ChoiceField(choices=PROJECTS, widget=forms.Select(attrs={'class':'form-control'}))

class AddProjectForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    deadline = forms.DateField(required=False, widget=forms.DateInput(attrs={'type':'date', 'class':'form-control date-edit', 'value':timezone.now().strftime("%Y/%m/%d")}))
