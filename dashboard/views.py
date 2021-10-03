from django.shortcuts import render, redirect
from .models import *
from user.views import *
import requests
import sys
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from subprocess import run, PIPE
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
import os
from pathlib import Path
# Create your views here.

# Dashboard
BASE_DIR = Path(__file__).resolve().parent.parent


def dashboard(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect(userLogin)
    context = {
        'username': request.user.username
    }
    print(context['username'])
    return render(request, 'dashboard/index.html', context)


def adsense(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect(userLogin)
    if request.method == "POST":
        file = request.FILES.get('file')
        if file is not None:
            Adsense.objects.create(file=file)
    data = Adsense.objects.all()
    context = {
        "data": data,
        'username': request.user.username
    }
    return render(request, 'dashboard/adsense.html', context)


def premium(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect(userLogin)
    if request.method == "POST":
        file = request.FILES.get('file')
        if file is not None:
            Premium.objects.create(file=file)
    data = Premium.objects.all()
    context = {
        "data": data,
        'username': request.user.username
    }
    return render(request, 'dashboard/premium.html', context)


def super(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect(userLogin)
    if request.method == "POST":
        file = request.FILES.get('file')
        if file is not None:
            Super.objects.create(file=file)
    data = Super.objects.all()
    context = {
        "data": data,
        'username': request.user.username
    }
    return render(request, 'dashboard/super.html', context)


def deleteAdsense(request, id):
    if not request.user.is_authenticated:
        return redirect(userLogin)
    file = Adsense.objects.get(id=id)
    if file is not None:
        file.delete()
        return redirect(adsense)


def deletePremium(request, id):
    if not request.user.is_authenticated:
        return redirect(userLogin)
    file = Premium.objects.get(id=id)
    if file is not None:
        file.delete()
        return redirect(premium)


def deleteSuper(request, id):
    if not request.user.is_authenticated:
        return redirect(userLogin)
    file = Super.objects.get(id=id)
    if file is not None:
        file.delete()
        return redirect(super)


def adsenseMerged(request, *args, **kwargs):
    run([sys.executable, 'media/panda/merge.py', 'csv'], shell=False, stdout=PIPE)
    run([sys.executable, 'media/panda/merge.py', 'super'], shell=False, stdout=PIPE)
    run([sys.executable, 'media/panda/merge.py', 'premium'], shell=False, stdout=PIPE)
    run([sys.executable, 'media/panda/process.py'], shell=False, stdout=PIPE)
    run([sys.executable, 'media/panda/process-s.py'], shell=False, stdout=PIPE)
    run([sys.executable, 'media/panda/process-p.py'], shell=False, stdout=PIPE)
    run([sys.executable, 'media/panda/total.py'], shell=False, stdout=PIPE)
    try:
        f = open(os.path.join(BASE_DIR, 'media/csv/output/merge.csv.gz'))
        # Do something with the file
        return redirect('/media/csv/output/merge.csv.gz')
    except IOError:
        return redirect(adsense)
    finally:
        f.close()

def adsenseProcessed(request, *args, **kwargs):
    run([sys.executable, 'media/panda/merge.py', 'csv'], shell=False, stdout=PIPE)
    run([sys.executable, 'media/panda/merge.py', 'super'], shell=False, stdout=PIPE)
    run([sys.executable, 'media/panda/merge.py', 'premium'], shell=False, stdout=PIPE)
    run([sys.executable, 'media/panda/process.py'], shell=False, stdout=PIPE)
    run([sys.executable, 'media/panda/process-s.py'], shell=False, stdout=PIPE)
    run([sys.executable, 'media/panda/process-p.py'], shell=False, stdout=PIPE)
    run([sys.executable, 'media/panda/total.py'], shell=False, stdout=PIPE)
    try:
        f = open(os.path.join(BASE_DIR, 'media/csv/output/partners.csv.gz'))
        # Do something with the file
        return redirect('/media/csv/output/partners.csv.gz')
    except IOError:
        return redirect(adsense)
    finally:
        f.close()
        


def premiumMerged(request, *args, **kwargs):
    run([sys.executable, 'media/panda/merge.py', 'csv'], shell=False, stdout=PIPE)
    run([sys.executable, 'media/panda/merge.py', 'super'], shell=False, stdout=PIPE)
    run([sys.executable, 'media/panda/merge.py', 'premium'], shell=False, stdout=PIPE)
    run([sys.executable, 'media/panda/process.py'], shell=False, stdout=PIPE)
    run([sys.executable, 'media/panda/process-s.py'], shell=False, stdout=PIPE)
    run([sys.executable, 'media/panda/process-p.py'], shell=False, stdout=PIPE)
    run([sys.executable, 'media/panda/total.py'], shell=False, stdout=PIPE)
    try:
        f = open(os.path.join(BASE_DIR, 'media/premium/output/merge.csv.gz'))
        # Do something with the file
        return redirect('/media/premium/output/merge.csv.gz')
    except IOError:
        return redirect(premium)
    finally:
        f.close()

def premiumProcessed(request, *args, **kwargs):
    run([sys.executable, 'media/panda/merge.py', 'csv'], shell=False, stdout=PIPE)
    run([sys.executable, 'media/panda/merge.py', 'super'], shell=False, stdout=PIPE)
    run([sys.executable, 'media/panda/merge.py', 'premium'], shell=False, stdout=PIPE)
    run([sys.executable, 'media/panda/process.py'], shell=False, stdout=PIPE)
    run([sys.executable, 'media/panda/process-s.py'], shell=False, stdout=PIPE)
    run([sys.executable, 'media/panda/process-p.py'], shell=False, stdout=PIPE)
    run([sys.executable, 'media/panda/total.py'], shell=False, stdout=PIPE)
    try:
        f = open(os.path.join(BASE_DIR, 'media/premium/output/partners.csv.gz'))
        # Do something with the file
        return redirect('/media/premium/output/partners.csv.gz')
    except IOError:
        return redirect(premium)
    finally:
        f.close()
        

def superMerged(request, *args, **kwargs):
    run([sys.executable, 'media/panda/merge.py', 'csv'], shell=False, stdout=PIPE)
    run([sys.executable, 'media/panda/merge.py', 'super'], shell=False, stdout=PIPE)
    run([sys.executable, 'media/panda/merge.py', 'premium'], shell=False, stdout=PIPE)
    run([sys.executable, 'media/panda/process.py'], shell=False, stdout=PIPE)
    run([sys.executable, 'media/panda/process-s.py'], shell=False, stdout=PIPE)
    run([sys.executable, 'media/panda/process-p.py'], shell=False, stdout=PIPE)
    run([sys.executable, 'media/panda/total.py'], shell=False, stdout=PIPE)
    try:
        f = open(os.path.join(BASE_DIR, 'media/super/output/merge.csv.gz'))
        # Do something with the file
        return redirect('/media/super/output/merge.csv.gz')
    except IOError:
        return redirect(super)
    finally:
        f.close()

def superProcessed(request, *args, **kwargs):
    run([sys.executable, 'media/panda/merge.py', 'csv'], shell=False, stdout=PIPE)
    run([sys.executable, 'media/panda/merge.py', 'super'], shell=False, stdout=PIPE)
    run([sys.executable, 'media/panda/merge.py', 'premium'], shell=False, stdout=PIPE)
    run([sys.executable, 'media/panda/process.py'], shell=False, stdout=PIPE)
    run([sys.executable, 'media/panda/process-s.py'], shell=False, stdout=PIPE)
    run([sys.executable, 'media/panda/process-p.py'], shell=False, stdout=PIPE)
    run([sys.executable, 'media/panda/total.py'], shell=False, stdout=PIPE)
    try:
        f = open(os.path.join(BASE_DIR, 'media/super/output/partners.csv.gz'))
        # Do something with the file
        return redirect('/media/super/output/partners.csv.gz')
    except IOError:
        return redirect(super)
    finally:
        f.close()
        

def total(request, *args, **kwargs):
    run([sys.executable, 'media/panda/merge.py', 'csv'], shell=False, stdout=PIPE)
    run([sys.executable, 'media/panda/merge.py', 'super'], shell=False, stdout=PIPE)
    run([sys.executable, 'media/panda/merge.py', 'premium'], shell=False, stdout=PIPE)
    run([sys.executable, 'media/panda/process.py'], shell=False, stdout=PIPE)
    run([sys.executable, 'media/panda/process-s.py'], shell=False, stdout=PIPE)
    run([sys.executable, 'media/panda/process-p.py'], shell=False, stdout=PIPE)
    run([sys.executable, 'media/panda/total.py'], shell=False, stdout=PIPE)
    try:
        f = open(os.path.join(BASE_DIR, 'media/total.csv.gz'))
        # Do something with the file
        return redirect('/media/total.csv.gz')
    except IOError:
        return redirect(dashboard)
    finally:
        f.close()