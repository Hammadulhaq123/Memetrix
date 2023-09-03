from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def logout_page(request):
    logout(request)
    return redirect("/login/")


def log_in(request):
    if request.method == "POST":
        data = request.POST
        username = data.get("username")
        password = data.get("password")

        user = User.objects.filter(username=username).exists()
        if not user:
            messages.info(request, "Invalid Username.")
            return redirect("/login/")

        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request, "Invalid Password.")
            return redirect("/login/")

        else:
            login(request, user)
            return redirect("/feeds/")
    if request.user.is_authenticated:
        return redirect("/feeds/")
    else:
        return render(request, "login.html", context={"title": "MemeTrix | Login"})


def sign_up(request):
    if request.method == "POST":
        data = request.POST
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        if User.objects.filter(username=username).exists():
            messages.info(request, "Username already exists!")
            return redirect("/signup/")

        user = User.objects.create(
            first_name=first_name, last_name=last_name, username=username, email=email
        )
        user.set_password(password)
        user.save()

        messages.success(request, "Account created succesfully!")

        redirect_feed = authenticate(username=username, password=password)
        login(request, redirect_feed)
        return redirect("/feeds/")

    if request.user.is_authenticated:
        return redirect("/feeds/")
    else:
        return render(
            request, "signup.html", context={"title": "MemeTrix | Join the memeclub"}
        )


def home(request):
    if request.user.is_authenticated:
        return redirect("/feeds/")
    else:
        return render(
            request,
            "home.html",
            context={"title": "MemeTrix | A Social platform for memer's"},
        )
