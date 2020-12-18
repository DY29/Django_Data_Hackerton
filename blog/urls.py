from django.urls import path
from . import views
urlpatterns = [
    path('', views.map, name='map'),
    path('intro/', views.intro, name='intro'),
    path('emojomo/', views.emojomo, name='emojomo'),
    path('team/', views.team, name='team'),
    path('yaksuto/', views.yaksuto, name='yaksuto'),
]

