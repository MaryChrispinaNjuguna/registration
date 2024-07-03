from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns=[
    path('', views.home, name='home'),
     path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('register/', views.register_view, name='register'),
]