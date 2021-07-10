
from django.urls import path

from . import views

app_name = "todo"

urlpatterns = [

        path('add/task/', views.add_task, name="add_task"),
        path('add/project/', views.add_project, name="add_project"),
]
