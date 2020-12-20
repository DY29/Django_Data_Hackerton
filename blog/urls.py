from django.urls import path
from . import views
urlpatterns = [
    path('intro/', views.intro, name='intro'),
    path('emojomo/', views.emojomo, name='emojomo'),
    path('team/', views.team, name='team'),
    path('map/', views.map, name='map'),
    path('', views.home, name='home'),
]

