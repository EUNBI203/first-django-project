from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('artii/', views.artii),
    path('artii_result/', views.artii_result),
    path('num_push/', views.num_push),
    path('num_pull/', views.num_pull),
]