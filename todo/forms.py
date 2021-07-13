
from django import forms
from django.utils import timezone

from .models import Task, Project

class AddTaskForm(forms.Form):

    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    doer = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    project = forms.Field(widget=forms.Select(attrs={'id':'select_project', 'class':'form-control'}))

class AddProjectForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    deadline = forms.DateField(required=False, widget=forms.DateInput(attrs={'type':'date', 'class':'form-control date-edit', 'value':timezone.now().strftime("%Y/%m/%d")}))
