# Django Weather App

## Overview
The Django Weather App is a simple web application that allows users to check the current weather of any city by fetching real-time data from the OpenWeatherMap API.

## Features
- Search weather by city name.
- Display temperature, weather condition, and an icon representing the weather.
- Error handling for invalid city names or network issues.

## Technologies Used
- Django (Python Framework)
- HTML, CSS (Frontend UI)
- OpenWeatherMap API
- Requests library (for API calls)

## Usage
1. Open the browser and go to `http://127.0.0.1:8000/`
2. Enter a city name and click the "Get Weather" button.
3. The app will display the current temperature, weather description, and an icon representing the weather.

## Project Structure
```
django-weather-app/
│-- config/          # Django project settings
│-- weather/         # Main weather app
│   ├── templates/   # HTML templates
│   ├── views.py     # Main logic for fetching weather data
│-- manage.py        # Django command-line tool
│-- requirements.txt # Project dependencies
```



