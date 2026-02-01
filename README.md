# HourlyChime with Weather

This Python project runs a background service on Windows that announces the current time and weather conditions at the top of every hour. It features a "wake-up" delay to prevent audio clipping on Realtek drivers and uses Open-Meteo for reliable, coordinate-based weather data.

## Features

* Hourly Announcements: Automatically chimes and speaks at the start of every hour.
* Weather Integration: Fetches real-time temperature and conditions for Columbus, OH via the Open-Meteo API.
* Audio Stability: Includes a 1.5-second pre-chime delay to ensure laptop speakers (like the Predator Helios 300) are fully initialized.
* Descriptive Weather: Maps WMO codes to natural language, including explanations for phenomena like rime fog.
* Graceful Exit: Properly handles Ctrl+C to shut down the background scheduler immediately.

## Installation

1. Install dependencies:

    ```pip install pyttsx3 requests apscheduler```

## How to Run

### 1. Standard Execution (Terminal)

To run the script and keep the terminal window open (best for testing):

    python main.py

*To exit, simply press Ctrl+C in the terminal.*

### 2. Run in the Background (No Window)

If you want the chime to run without a visible command prompt window:

1. Rename your file from main.py to main.pyw.
2. Double-click main.pyw. Windows will use pythonw.exe to run it silently.

*To stop it in this mode, you must find "Python" in the Task Manager and end the task.*

### 3. Run Automatically at Startup

To have the chime start every time you log into your laptop:

1. Press Win + R, type shell:startup, and hit Enter.
2. Right-click your main.py (or main.pyw) file and select Create Shortcut.
3. Move that shortcut into the Startup folder you just opened.
