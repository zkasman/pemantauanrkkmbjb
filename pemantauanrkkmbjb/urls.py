"""
pemantauanrkkmbjb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('dashboard', TemplateView.as_view(template_name='dashboard.html'), name='dashboard'),
    path('lembangan', TemplateView.as_view(template_name='lembangan.html'), name='lembangan'),
    path('sublembangan', TemplateView.as_view(template_name='sublembangan.html'), name='sublembangan'),
    path('sungai', TemplateView.as_view(template_name='sungai.html'), name='sungai'),
    path('gunatanahsemasa', TemplateView.as_view(template_name='gunatanahsemasa.html'), name='gunatanahsemasa'),
    path('rumasangunatanah', TemplateView.as_view(template_name='rumusangunatanah.html'), name='rumusangunatanah'),
    path('isumasalah', TemplateView.as_view(template_name='isumasalah.html'), name='isumasalah'),
    path('potensiprospek', TemplateView.as_view(template_name='potensiprospek.html'), name='potensiprospek'),
    path('zontindakan', TemplateView.as_view(template_name='zontindakan.html'), name='zontindakan'),
    path('projekrkk/', include('projekrkk.urls')),
    path('admin/', admin.site.urls),
]

admin.site.site_header  =  "Sistem Pengurusan & Pemantauan RKK"  
admin.site.site_title  =  "Sistem Pengurusan & Pemantauan RKK"
admin.site.index_title  =  "Pentadbir Sistem"