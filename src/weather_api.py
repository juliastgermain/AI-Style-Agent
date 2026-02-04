"""
OpenWeather API integration for weather data
"""
import requests
from config import OPENWEATHER_API_KEY, WEATHER_UNITS

class WeatherAPI:
    """
    Fetches weather data from OpenWeather API
    """
    BASE_URL = "https://api.openweathermap.org/data/2.5"
    
    def __init__(self, api_key=None):
        self.api_key = api_key or OPENWEATHER_API_KEY
        
    def get_current_weather(self, location):
        """
        Get current weather for a location
        
        Args:
            location (str): City name or coordinates
            
        Returns:
            dict: Weather data
        """
        # TODO: Implement API call
        # Week 2 implementation
        pass
        
    def get_forecast(self, location, days=7):
        """
        Get weather forecast
        
        Args:
            location (str): City name or coordinates
            days (int): Number of days to forecast
            
        Returns:
            dict: Forecast data
        """
        # TODO: Implement API call
        # Week 2 implementation
        pass