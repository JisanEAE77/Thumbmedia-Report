from typing import Dict, List, Any
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from dashboard.models import *
from django.contrib.auth import authenticate, login, logout
from password_validator import PasswordValidator
import re


# Create your views here.

# Registration Page


def userRegistration(request, *args, **kwargs):
    users = User.objects.all()
    userlist = [user.username for user in users]
    emaillist = [user.email for user in users]

    context = {
        "error": [],
    }

    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        username = request.POST.get('username')
        username = username.lower()
        password = request.POST.get('password')
        email = request.POST.get('email')
        email = email.lower()

        if username not in userlist and email not in emaillist and checkEmail(email) and checkPassword(password):
            print(username, email, password)
            User.objects.create_user(username=username, email=email, password=password)
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("/")
        else:
            if username in userlist:
                context["error"].append("Username already exists, please choose another!")
            if email in emaillist and checkEmail(email):
                context["error"].append("This E-mail is already in use, please try again with another e-mail!")
            if not checkEmail(email):
                context["error"].append("Invalid E-mail format, enter a valid E-mail!")
            if not checkPassword(password):
                context["error"].append("Weak password! Your password should contain at least one lowercase letter, one uppercase letter, one numeric digit, one special character and must be at least 6 character long!")

    return render(request, "user/sign-up.html", context)


# Login Page


def userLogin(request, *args, **kwargs):
    users = User.objects.all()
    userlist = [user.username for user in users]
    context = {
        "error": [],
    }
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        username = request.POST.get('username')
        username = username.lower()
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        if username not in userlist:
            context["error"].append("Username doesn't exist, please enter a valid username!")
        else:
            context["error"].append("Wrong password for this user, try again with correct username & password!")

    return render(request, "user/login.html", context)


# Username Validator


def validateusername(request, username):
    users = User.objects.all()
    userlist = [user.username for user in users]
    username = username.lower()

    if username in userlist:
        data = {
            "response": "VALID"
        }
        return JsonResponse(data)
    data = {
        "response": "INVALID"
    }
    return JsonResponse(data)


# Email Validator


def validateemail(request, email):
    users = User.objects.all()
    emaillist = [user.email for user in users]
    email = email.lower()

    if email in emaillist:
        data = {
            "response": "VALID"
        }
        return JsonResponse(data)
    data = {
        "response": "INVALID"
    }
    return JsonResponse(data)


# Login Validator


def validatelogin(request, username, password):
    username = username.lower()
    user = authenticate(username=username, password=password)

    if user is not None:
        data = {
            "response": "VALID"
        }
        return JsonResponse(data)

    data = {
        "response": "INVALID"
    }
    return JsonResponse(data)


# temporary dashboard


def dashboard(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("/login")
    return render(request, "dashboard/dashboard.html")


# Registration Page

# Email Format Validator


def checkEmail(email):
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    if re.search(regex, email):
        return True
    else:
        return False

# Password Strength Check


def checkPassword(password):
    schema = PasswordValidator()
    schema \
        .min(6) \
        .max(100000) \
        .has().uppercase() \
        .has().lowercase() \
        .has().digits() \
        .has().symbols() \
        .has().no().spaces() \

    if schema.validate(password):
        return True
    else:
        return False


def logOut(request):
    logout(request)
    return redirect('/')
