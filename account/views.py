
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse

from .forms import LoginForm, UserRegisterationForm, UserEditForm

@login_required
def dashboard(req):

    user = User.objects.get(profile_user=req.user)
    
    return render(req, 'account/dashboard.html', {'user':user})

@login_required
def edit_profile(req):

    user = req.user
    
    data = {
        
        'first_name':user.first_name,
        'last_name':user.last_name,
        'email':user.email,
    }

    if req.method == "POST":
        edit_form = UserEditForm(req.POST)

        if edit_form.is_valid():

            cd = edit_form.cleaned_data
            user.first_name = cd['first_name']
            user.last_name = cd['last_name']
            user.email = cd['email']

            user.save()

            return HttpResponseRedirect(reverse("account:dashboard"))
    else:
        edit_form = UserEditForm(data=data)

    return render(req, 'account/user_edit.html', { 'edit_form':edit_form })

def register(req):

    if req.method == "POST":

        user_form = UserRegisterationForm(req.POST)
        if user_form.is_valid():

            cd = user_form.cleaned_data

            new_user_first_name = cd['first_name']
            new_user_last_name = cd['last_name']
            new_user_username = cd['username']
            new_user_email = cd['email']

            new_user = User.objects.create(first_name=new_user_first_name,
                                    last_name=new_user_last_name,
                                    username=new_user_username,
                                    email=new_user_email)
            new_user.set_password(cd['password'])
            new_user.save()

            login(req, new_user)
            return HttpResponseRedirect(reverse("account:dashboard"))
    else:
        user_form = UserRegisterationForm()

    return render(req, 'account/register.html', {'user_form':user_form})
            
def user_login(req):

    if req.method == "POST":

        next_url = req.POST.get('next','/')
        form = LoginForm(req.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(req, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(req, user)
                    if next_url:
                        return HttpResponseRedirect(next_url)
                    else:
                        return HttpResponseRedirect(reverse("account:dashboard"))
                else:
                    return render(req, "account/not_active_error.html", {})
            else:
                return render(req, "account/login_failed.html", {})
        else:
            return render(req, "account/Invalid_form.html", {})
    else:
        form = LoginForm()

    return render(req, "account/login.html", {'form':form})

def user_logout(req):
    logout(req)
    return HttpResponseRedirect(reverse("account:login"))

