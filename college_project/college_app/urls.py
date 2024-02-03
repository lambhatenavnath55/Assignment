from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('create_professor/', views.create_professor, name='create_professor'),
    path('professor_info/', views.professor_info, name='professor_info'),
]