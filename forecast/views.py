from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
import os
from forecast.models import Mood
from forecast.forms import MoodForm
from dotenv import load_dotenv
from django.views import View
import json
load_dotenv()

WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')

class WeatherView(View):
    def get(self,request):
        current_weather = requests.get('http://api.openweathermap.org/data/2.5/weather?q=San Francisco&units=metric&appid=5956f6201c4fa8d82540e16c891313bb')
        response = current_weather.json()
        weather = response['weather']
        description = weather[0]['description']
        main = response['main']
        temp = main['temp']
        if description == 'few clouds':
            description = ' partly cloudy'
        return render(request, 'forecast/home.html', {
            "response": response,
            "description": description,
            "weather": weather,
            "main": main,
            "temp": temp 


        })
class MoodView(View):
    model = Mood
    def post(self,request):
        form = MoodForm(request.POST)
        if form.is_valid():
            added = form.save()
            added.save()
            print(added)
        print("lllllllllll")
        return render(request, 'forecast/thank-you.html')
        