
from django.urls import path

from . import views

app_name = "todo"

urlpatterns = [

        path('add/task/', views.add_task, name="add_task"),
        path('add/project/', views.add_project, name="add_project"),
        path('projects/', views.project_list, name="project_list"),
        path('ajax/get_projects', views.get_projects, name="get_projects"),
]
