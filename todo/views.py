from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Task, Project
from .forms import AddTaskForm, AddProjectForm

# Create your views here.
@login_required
def add_task(req):

    if req.method == "POST":
        form = AddTaskForm(req.POST)
        if form.is_valid():
            cd = form.cleaned_data
            project = None
            if cd['project'] != '0':
                project = Project.objects.get(pk=cd['project'])

            new_task = Task.objects.create(name=cd['name'], description=cd['description'], doer=cd['doer'],
                                    isDone=False, project=project, user=req.user)
        return HttpResponseRedirect(reverse("account:dashboard"))
    else:
        form = AddTaskForm()

    return render(req, 'todo/add_task.html', {'form':form})

@login_required
def add_project(req):

    if req.method == "POST":
        form = AddProjectForm(req.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            new_project = Project.objects.create(name=cd['name'], description=cd['description'], deadline=cd['deadline'], user=req.user)
        return HttpResponseRedirect(reverse("account:dashboard"))
    else:
        form = AddProjectForm()

    return render(req, 'todo/add_project.html', {'form':form})

def task_list(req, project_id):
    pass

def project_list(req):

    list_project = Project.objects.all()
    return render(req, 'todo/project_list.html', { project_list:'project_list' })
