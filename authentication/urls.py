"""
URL configuration for authentication project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from base import views 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name='home'),
    path('l',views.Login,name='login'),
    path('r',views.Registration,name='registration'),
    path('d',views.Dashboard,name='dashboard'),
    path('lo',views.Logout,name='logout'),
    path('b',views.Blog_post,name='blog_post'),
    path('bd',views.BlogDetials,name='blogdetials'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
