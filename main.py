import pyttsx3
from datetime import datetime

def announce_time_female():
    engine = pyttsx3.init()

    # 1. Get the list of available voices
    voices = engine.getProperty('voices')

    # 2. Set the voice to the female one
    # index 0 is usually Microsoft David (Male)
    # index 1 is usually Microsoft Zira (Female)
    engine.setProperty('voice', voices[1].id)

    # 3. Optional: Slow down the speed for a more natural sound
    engine.setProperty('rate', 150) 

    # 4. Get and format the time
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")
    message = f"The current time is {current_time}."
    
    print(f"Speaking: {message}")
    engine.say(message)
    engine.runAndWait()

if __name__ == "__main__":
    announce_time_female()