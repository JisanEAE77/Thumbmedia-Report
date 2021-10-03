"""thumbmedia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from user.views import *
from dashboard.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('total/', total, name='total'),
    path('adsense/', adsense, name='adsense'),
    path('adsense/merged', adsenseMerged, name='adsenseMerged'),
    path('adsense/processed', adsenseProcessed, name='adsenseProcessed'),
    path('premium/', premium, name='premium'),
    path('premium/merged', premiumMerged, name='premiumMerged'),
    path('premium/processed', premiumProcessed, name='premiumProcessed'),
    path('super/', super, name='super'),
    path('super/merged', superMerged, name='superMerged'),
    path('super/processed', superProcessed, name='adsenseProcessed'),
    path('user/', include('user.urls')),
    path('validateusername/<str:username>', validateusername, name="validateusername"),
    path('validateemail/<str:email>', validateemail, name="validateemail"),
    path('validatelogin/<str:username>/<str:password>', validatelogin, name="validatelogin"),
    path('adsense/<int:id>', deleteAdsense, name='deleteAdsense'),
    path('premium/<int:id>', deletePremium, name='deletePremium'),
    path('super/<int:id>', deleteSuper, name='deleteSuper'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
