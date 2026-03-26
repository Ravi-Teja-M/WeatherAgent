import streamlit as st
import requests
from agent import get_weather_and_time

# Page configuration
st.set_page_config(
    page_title="WeatherAgent GUI",
    page_icon="🌤️",
    layout="centered",
)

# Custom CSS for a premium look
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        color: white;
    }
    .stApp {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
    }
    .weather-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 30px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        margin-top: 20px;
    }
    .metric-label {
        font-size: 0.9rem;
        color: #a0aec0;
        margin-bottom: 5px;
    }
    .metric-value {
        font-size: 2.5rem;
        font-weight: bold;
        color: #ffffff;
    }
    .city-header {
        font-size: 2rem;
        font-weight: 800;
        margin-bottom: 10px;
        background: linear-gradient(to right, #00c6ff, #0072ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .time-display {
        color: #63b3ed;
        font-family: 'Courier New', Courier, monospace;
        font-size: 1.1rem;
    }
    </style>
""", unsafe_allow_html=True)

# App Header
st.title("🌤️ WeatherAgent")
st.markdown("Enter a city name to get real-time weather and local time (with DST handling).")

# Input section
with st.container():
    col1, col2 = st.columns([3, 1])
    with col1:
        city = st.text_input("City Name", placeholder="e.g. London, Tokyo, New York...", label_visibility="collapsed")
    with col2:
        search_button = st.button("Get Weather", use_container_width=True)

if search_button or city:
    if city:
        with st.spinner(f"Fetching weather for {city}..."):
            data = get_weather_and_time(city)
            
            if "error" in data:
                st.error(data["error"])
            else:
                # Success Display
                st.markdown(f'<div class="weather-card">', unsafe_allow_html=True)
                
                st.markdown(f'<div class="city-header">{data["city"].title()}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="time-display">🕒 {data["time"]}</div>', unsafe_allow_html=True)
                
                st.divider()
                
                m1, m2 = st.columns(2)
                with m1:
                    st.markdown('<div class="metric-label">Temperature</div>', unsafe_allow_html=True)
                    st.markdown(f'<div class="metric-value">{data["temperature"]}°C</div>', unsafe_allow_html=True)
                with m2:
                    st.markdown('<div class="metric-label">Humidity</div>', unsafe_allow_html=True)
                    st.markdown(f'<div class="metric-value">{data["humidity"]}%</div>', unsafe_allow_html=True)
                
                st.markdown(f'<p style="margin-top:20px; color:#cbd5e0;">{data["description"]}</p>', unsafe_allow_html=True)
                
                st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning("Please enter a city name.")

# Footer
st.markdown("---")
st.caption("Powered by Google ADK & Open-Meteo API")
