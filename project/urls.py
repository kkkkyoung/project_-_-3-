from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload, name = 'upload'),
    path('check/', views.check, name = 'check'),
    path('final_check/', views.final_check, name = 'final_check'),
]