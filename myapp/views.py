import requests
from django.shortcuts import render
from .models import City

def home(request):
    return render(request, "index.html")

def weather(request):
    if request.method == "POST":
        City_name = request.POST.get('mycity')
        obj = City()
        obj.name = City_name
        obj.save()
        api_key = 'f12b3313541702a2c78470c5249a6a68'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={City_name}&appid={api_key}&units=metric'
        response = requests.get(url)
        data = response.json()
        
       
        if 'main' in data and 'temp' in data['main']:
            weather_data = {
                'city': City_name,
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
                
            }
            return render(request, 'index.html', {'weather_data': weather_data})
        else:
            error_message = "Invalid city name. Please enter a valid city name."
            return render(request, 'index.html', {'error_message': error_message})

    return render(request, 'index.html')
