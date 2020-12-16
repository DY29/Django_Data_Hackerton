from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('intro/', views.intro, name='intro'),
    path('emojomo/', views.emojomo, name='emojomo'),
]