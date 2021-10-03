from django.urls import path
from .views import *

urlpatterns = [
    path('login/', userLogin, name='userLogin'),
    path('logout/', logOut, name='userLogin'),
    path('sign-up/', userRegistration, name='userRegistration'),
]
