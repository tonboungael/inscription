from django.urls import path
from . import views

urlpatterns = [
    path('Don/', views.suiviDon, name='suiviDon'),
    
]