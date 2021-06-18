from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Task, Project
from .forms import AddTaskForm

# Create your views here.
def add_task(req):

    if req.method == "POST":
        form = AddTaskForm(data=req.POST)
        if form.is_valid:
            form.save()
        return HttpResponseRedirect(reverse("account:dashboard"))
    else:
        form = AddTaskForm()

    return render(req, 'todo/add_task.html', {'form':form})

