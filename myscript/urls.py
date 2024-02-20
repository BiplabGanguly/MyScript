"""
URL configuration for myscript project.

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
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login_page,name = "login"),
    path('post_login/',views.post_login_page,name="post_login"),
    path('index/<uid>/',views.home_page,name="index"),
    path('myscript/<sid>/',views.script_page,name='myscript'),
    path('script/<uid>/',views.post_script_page,name='script'),
    path('delete_script/<sid>/',views.delete_script,name="delete_script"),
    path('logout/',views.log_out,name='logout'),
    
]
