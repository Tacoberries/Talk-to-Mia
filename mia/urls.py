from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='mia-home'),
    path('about/', views.about, name='mia-about'),
    path('api/mia/', views.mia_api, name='mia_api'),
]