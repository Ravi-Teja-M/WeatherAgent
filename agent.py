import requests
import zoneinfo
from datetime import datetime
from google.adk.agents.llm_agent import Agent

def get_weather_and_time(city: str) -> str:
    """
    Fetches the current weather and local time for a given city.
    Automatically handles Daylight Saving Time (DST).
    """
    try:
        # 1. Geocode the city to get coordinates and timezone
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"
        geo_resp = requests.get(geo_url).json()

        if not geo_resp.get('results'):
            return f"Error: Could not find city: {city}"

        result = geo_resp['results'][0]
        lat, lon = result['latitude'], result['longitude']
        timezone_name = result['timezone'] # e.g., 'America/New_York'

        # 2. Get current weather
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m&timezone={timezone_name}"
        weather_resp = requests.get(weather_url).json()

        if 'current' not in weather_resp:
            return f"Error: Could not retrieve weather data for {city}."

        temp = weather_resp['current']['temperature_2m']
        humidity = weather_resp['current']['relative_humidity_2m']

        # 3. Get current local time (handles DST automatically via ZoneInfo)
        local_time = datetime.now(zoneinfo.ZoneInfo(timezone_name))
        time_str = local_time.strftime("%Y-%m-%d %H:%M:%S %Z")

        return (f"The current weather in {city} is {temp}°C with {humidity}% humidity. "
                f"The local time is {time_str}.")
    except Exception as e:
        return f"An error occurred while fetching data for {city}: {str(e)}"

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge. Use the provided tools to fetch weather and time when asked.',
    tools=[get_weather_and_time]
)
