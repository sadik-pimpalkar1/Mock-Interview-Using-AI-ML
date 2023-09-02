from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
# from app.views import home

urlpatterns = [
    path('', views.home, name="home"),
    path('upload_resume/', views.upload_resume, name="upload_resume"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
]
