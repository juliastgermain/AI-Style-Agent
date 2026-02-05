# AI Style Agent 

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Status](https://img.shields.io/badge/status-in%20development-yellow.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

> **AI-powered personal style assistant that recommends daily outfits based on weather, calendar events, and personal preferences**

**Project Status:** Week 1 - Foundation & Setup  
**Target Completion:** March 9, 2025  
**Live Demo:** Coming soon!

## 🎯 Project Overview

Ever spent too long deciding what to wear? This AI agent solves that by combining:
- **Computer Vision** (CLIP) to analyze your wardrobe
- **Weather Data** to suggest appropriate clothing
- **Calendar Context** to match outfits to your schedule
- **LLM Reasoning** to provide styling advice

## ✨ Features (Planned)

- [ ] **Smart Wardrobe Analysis**: Upload photos of your clothes, AI categorizes them
- [ ] **Weather-Aware Recommendations**: Integrates real-time weather data
- [ ] **Calendar Integration**: Suggests outfits based on your daily schedule
- [ ] **Style Learning**: Remembers your preferences and feedback
- [ ] **Outfit Rating**: Scores outfits on formality, color coordination, seasonality
- [ ] **Interactive Web Interface**: Easy-to-use Streamlit app

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Computer Vision**: CLIP (Hugging Face Transformers)
- **LLM**: OpenAI GPT-4 / Anthropic Claude
- **APIs**: OpenWeather API, Google Calendar API
- **ML Framework**: PyTorch
- **Deployment**: Hugging Face Spaces (planned)

## 📊 Project Roadmap

### Week 1: Foundation ✅ (Current)
- [x] Project setup and structure
- [x] README and documentation
- [ ] Environment configuration
- [ ] API key setup
- [ ] Basic Streamlit UI

### Week 2: Core Logic
- [ ] OpenWeather API integration
- [ ] Calendar input system
- [ ] Basic recommendation algorithm
- [ ] Weather-based outfit rules

### Week 3: Vision Component
- [ ] CLIP model integration
- [ ] Image upload functionality
- [ ] Clothing feature extraction
- [ ] Wardrobe database (JSON/SQLite)

### Week 4: LLM Integration
- [ ] Conversational interface
- [ ] Styling advice generation
- [ ] User preference learning
- [ ] Recommendation refinement

### Week 5: Polish & Deploy
- [ ] UI improvements
- [ ] Deploy to Hugging Face Spaces
- [ ] Create demo video
- [ ] Comprehensive documentation
- [ ] LinkedIn announcement

## 🚀 Quick Start

### Prerequisites
```bash
Python 3.9+
OpenAI/Anthropic API key
OpenWeather API key (free tier)
```

### Installation
```bash
# Clone the repository
git clone https://github.com/juliastgermain/AI-Style-Agent.git
cd AI-Style-Agent

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys
```

### Running the App
```bash
streamlit run src/app.py
```

## 📁 Project Structure
```
AI-Style-Agent/
├── src/
│   ├── app.py                      # Main Streamlit application
│   ├── weather_api.py              # OpenWeather API integration
│   ├── calendar_integration.py     # Calendar API/manual input
│   ├── outfit_recommender.py       # Recommendation logic
│   └── vision_model.py             # CLIP model for image analysis
├── data/
│   ├── wardrobe/                   # User's clothing photos
│   └── user_preferences/           # User style preferences
├── tests/                          # Unit tests
├── requirements.txt                # Dependencies
└── README.md                       # This file
```

## 🎨 How It Works

1. **User uploads photos** of clothing items
2. **CLIP model analyzes** each item (type, color, formality, season)
3. **Weather API fetches** current and forecast data
4. **Calendar provides** context about today's events
5. **Recommendation engine** selects optimal outfit
6. **LLM generates** styling tips and explanations

## 📧 Contact

**Julia St.Germain**  
📧 juliastg3rmain@gmail.com  
💼 [LinkedIn](https://linkedin.com/in/julia-st-germain-ai-ml)  
🔗 [GitHub](https://github.com/juliastgermain)



⭐ **If you find this project interesting, please star the repository!**

