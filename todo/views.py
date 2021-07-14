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
        return HttpResponseRedirect(reverse("todo:task_list"))
    else:
        form = AddTaskForm()

    return render(req, 'todo/add_task.html', {'form':form})

@login_required
def add_project(req):

    if req.method == "POST":
        form = AddProjectForm(req.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_project = Project.objects.create(name=cd['name'], description=cd['description'], deadline=cd['deadline'], user=req.user)
        return HttpResponseRedirect(reverse("todo:project_list"))
    else:
        form = AddProjectForm()

    return render(req, 'todo/add_project.html', {'form':form})

@login_required
def task_list(req):
    if req.method == "POST":
        username = req.POST.get('user')
        task_pk = req.POST.get('task_id')
        user = req.user
        if username == user.username:
            task = None
            try:
                task = Task.objects.get(pk=task_pk)
            except Task.DoesNotExist:
                pass
            if task and task.user == user:
                if req.POST.get('delete'):
                    task.delete()
                else:
                    task.isDone = False if task.isDone else True
                    task.save()
    task_list = Task.objects.filter(user=req.user).order_by("-submitDate")
    if req.GET.get('project'):
        try:
            project_pk = req.GET.get('project')
            task_list = task_list.filter(project__pk=project_pk)
        except ValueError:
            pass
    return render(req, 'todo/task_list.html', { 'task_list':task_list })

@login_required
def project_list(req):
    if req.method == "POST":
        username = req.POST.get('user')
        project_pk = req.POST.get('project_id')
        user = req.user
        if username == user.username:
            project = None
            try:
                project = Project.objects.get(pk=project_pk)
            except Project.DoesNotExist:
                pass
            if project and project.user == user:
                if req.POST.get('delete'):
                    project.delete()
                else:
                    project.isDone = False if project.isDone else True
                    project.save()
    project_list = Project.objects.filter(user=req.user).order_by("-submitDate")
    return render(req, 'todo/project_list.html', { 'project_list':project_list })

@login_required
def get_projects(req):
    username = req.GET.get('username')
    projects = list()
    if req.user.username == username:
        projects = Project.objects.filter(user=req.user)
    return render(req, 'todo/get_projects.html', { 'projects':projects })
