from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import messages

# Create your views here.


@login_required(redirect_field_name="login_required", login_url="/login/")
def profile(request, id):
    return render(request, "profile.html")


def update_name(request, id):
    pass


def update_pass(request, id):
    pass


def update_number(request, id):
    pass


def delete_account(request, id):
    try:
        queryset = User.objects.get(id=id)
        queryset.delete()
        logout(request)
        messages.success(request, "Account deleted succesfully!")
    except:
        messages.error(request, "Internal Server error")
    return redirect("/signup/")
