import pyttsx3
import python_weather
import asyncio
import winsound
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

async def chime():
    # Get the current time
    current_time = datetime.now().strftime("%I:%M %p")
    message = f"The current time is {current_time}."

    # Get the weather for Columbus
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        weather = await client.get('Columbus, OH')
        temp = weather.temperature
        desc = weather.description
        message += f" It is {temp} degrees and {desc}."

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150) 

    winsound.PlaySound("SystemNotification", winsound.SND_ALIAS)
    print(message)
    
    engine.say(message)
    engine.runAndWait()

def job():
    asyncio.run(chime())

if __name__ == '__main__':
    # Run once when starting
    job()

    scheduler = BlockingScheduler()
    scheduler.add_job(job, 'cron', minute=0)

    print("Scheduler started. Press Ctrl+C to exit.")
    scheduler.start()
