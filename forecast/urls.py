from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.WeatherView.as_view(), name='weatherview'),
    path('submit', views.MoodView.as_view(), name='moodview')
    
]