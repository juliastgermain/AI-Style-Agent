"""
AI Style Agent - Main Application
A personal AI assistant that recommends daily outfits
"""
import streamlit as st
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="AI Style Agent",
    page_icon="👔",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Header
st.title("🎨 AI Style Agent")
st.markdown("*Your personal AI-powered style assistant*")

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    location = st.text_input("Your Location", value="Boston, MA")
    
    st.markdown("---")
    st.markdown("### 📅 Today's Schedule")
    event = st.text_area("Events (one per line)", 
                         placeholder="9am - Team meeting\n2pm - Coffee with friend")
    
    st.markdown("---")
    st.markdown("### 🎯 Project Status")
    st.info("**Week 1**: Foundation & Setup")
    st.progress(10)

# Main content
tab1, tab2, tab3 = st.tabs(["🏠 Home", "👔 Wardrobe", "⚙️ Preferences"])

with tab1:
    st.header("Today's Outfit Recommendation")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 🌤️ Weather")
        st.info("Weather integration coming in Week 2!")
        
        st.markdown("### 👕 Recommended Outfit")
        st.warning("Outfit recommendations coming in Week 2!")
        
    with col2:
        st.markdown("### 📅 Your Schedule")
        if event:
            for line in event.split('\n'):
                if line.strip():
                    st.write(f"• {line}")
        else:
            st.write("No events scheduled")

with tab2:
    st.header("Your Wardrobe")
    st.info("Upload and manage your clothing items - Coming in Week 3!")
    
    uploaded_file = st.file_uploader(
        "Upload clothing photos",
        type=['png', 'jpg', 'jpeg'],
        accept_multiple_files=True
    )

with tab3:
    st.header("Style Preferences")
    st.info("Set your style preferences - Coming in Week 4!")
    
    style = st.selectbox(
        "Preferred Style",
        ["Casual", "Business Casual", "Formal", "Sporty", "Trendy"]
    )

# Footer
st.markdown("---")
st.markdown(
    "**AI Style Agent** | "
    f"Last updated: {datetime.now().strftime('%B %d, %Y')} | "
    "[GitHub](https://github.com/juliastgermain/AI-Style-Agent)"
)