import pyttsx3
import python_weather
import asyncio
import winsound
import time
import sys
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

async def chime():
    # Initialize engine early to wake up the driver
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)
    
    current_time = datetime.now().strftime("%I:%M %p")
    message = f"The current time is {current_time}."

    try:
        async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
            weather = await client.get('Columbus, OH')
            message += f" It is {weather.temperature} degrees and {weather.description}."
    except:
        pass # Fallback to time only if weather fails

    time.sleep(1.5)
    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {message}")
    engine.say(f" , {message}")
    engine.runAndWait()
    engine.stop()

def job():
    asyncio.run(chime())

if __name__ == '__main__':
    # Run once at startup
    job()
    
    # Switch to BackgroundScheduler so the main thread stays open
    scheduler = BackgroundScheduler()
    scheduler.add_job(job, 'cron', minute=0)
    scheduler.start()

    print("BackgroundScheduler started. Press Ctrl+C to exit.")

    # Main thread loop - this is what captures Ctrl+C reliably
    try:
        while True:
            time.sleep(1) # Sleep in small increments
    except (KeyboardInterrupt, SystemExit):
        print("Stopping scheduler...")
        scheduler.shutdown()
        sys.exit(0)
        