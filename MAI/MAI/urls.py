"""
URL configuration for amadeo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from os import stat
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from . import settings
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('cerebro.urls')),
    path("", include('editor.urls')),
    path("", include('usuarios.urls')),
    path("", include('login.urls')),
    path('', views.index, name= "index"),
    path('accounts/', include('allauth.urls')),
    path('', TemplateView.as_view(template_name="login.html")), 
]

if settings.DEBUG:
    urlpatterns += stat(settings.STATIC_URL, document_root=settings.STATIC_ROOT)