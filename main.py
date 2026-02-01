import pyttsx3
import requests
import asyncio
import winsound
import time
import sys
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

# Mapping WMO codes to clear, descriptive English
def get_weather_desc(code):
    wmo_codes = {
        0: "clear skies",
        1: "mainly clear skies",
        2: "partly cloudy skies",
        3: "overcast skies",
        45: "foggy conditions",
        48: "depositing rime fog, which means fog is freezing onto surfaces like trees and cars",
        51: "a light drizzle",
        53: "moderate drizzle",
        55: "dense drizzle",
        61: "slight rain",
        63: "moderate rain",
        65: "heavy rain",
        66: "light freezing rain",
        67: "heavy freezing rain",
        71: "slight snow fall",
        73: "moderate snow fall",
        75: "heavy snow fall",
        95: "a thunderstorm"
    }
    return wmo_codes.get(code, "fair conditions")

async def chime():
    # Initialize engine early to wake up the driver
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    # Using the second voice (index 1) which is usually clearer on laptop speakers
    engine.setProperty('voice', voices[1].id if len(voices) > 1 else voices[0].id)
    engine.setProperty('rate', 150)
    
    current_time = datetime.now().strftime("%I:%M %p")
    message = f"The current time is {current_time}."

    # Fetch Weather from Open-Meteo (Using Columbus, OH coordinates)
    try:
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": 39.9612,
            "longitude": -82.9988,
            "current": ["temperature_2m", "weather_code"],
            "temperature_unit": "fahrenheit",
            "timezone": "auto"
        }
        response = requests.get(url, params=params, timeout=5)
        data = response.json()["current"]
        
        temp = int(data["temperature_2m"])
        desc = get_weather_desc(data["weather_code"])
        message += f" It is {temp} degrees with {desc} in Columbus."
    except Exception as e:
        print(f"Weather error: {e}")
        message += " Weather data is currently unavailable."

    # Wake up the audio driver
    time.sleep(1.5) 
    
    # Play the alert sound
    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {message}")
    
    # The comma provides a small 'breath' for the speaker before starting
    engine.say(f" , {message}")
    engine.runAndWait()
    engine.stop()

def job():
    asyncio.run(chime())

if __name__ == '__main__':
    # Initial run upon starting the script
    job()

    # BackgroundScheduler lets the main thread listen for Ctrl+C
    scheduler = BackgroundScheduler()
    scheduler.add_job(job, 'cron', minute=0)
    scheduler.start()

    print("HourlyChime started. Press Ctrl+C to exit.")

    try:
        while True:
            # Short sleep keeps the CPU usage low and Ctrl+C responsive
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        print("\nStopping HourlyChime... Goodbye!")
        scheduler.shutdown()
        sys.exit(0)
        