import requests
from django.shortcuts import render

API_KEY = "your_api_key"
WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric"

def weather_view(request):
    weather_data = None
    error = None

    if request.method == "POST":
        city = request.POST.get("city")
        if city:
            try:
                response = requests.get(WEATHER_URL.format(city, API_KEY))
                data = response.json()
                if data["cod"] == 200:
                    weather_data = {
                        "city": city,
                        "temperature": data["main"]["temp"],
                        "description": data["weather"][0]["description"],
                        "icon": data["weather"][0]["icon"],
                    }
                else:
                    error = "City not found. Please try again."
            except requests.exceptions.RequestException:
                error = "Unable to fetch weather data. Please check your connection."

    return render(request, "weather.html", {"weather_data": weather_data, "error": error})
