
from django.urls import path, include

from . import views

app_name = "account"

urlpatterns = [

        path('login/', views.user_login, name = "login"),
        path('logout/', views.user_logout, name = "logout"),
        path('', views.dashboard, name = "dashboard"),
        path('register/', views.register, name = "register"),
        path('edit_profile/', views.edit_profile, name = "profile"),
]
