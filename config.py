"""
Configuration settings for AI Style Agent
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

# App Settings
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
DEFAULT_LOCATION = os.getenv("DEFAULT_LOCATION", "Boston, MA")

# Model Settings
CLIP_MODEL = "openai/clip-vit-base-patch32"
LLM_MODEL = "gpt-4"  # or "claude-3-sonnet-20240229"

# Paths
WARDROBE_DIR = "data/wardrobe"
PREFERENCES_DIR = "data/user_preferences"

# Weather Settings
WEATHER_UNITS = "imperial"  # fahrenheit
FORECAST_DAYS = 7