
from django.urls import path

from . import views

app_name = "todo"

urlpatterns = [

        path('add/', views.add_task, name="add"),
]
