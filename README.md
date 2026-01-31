# 🕒 Hourly Chime & Weather Announcer

A Python automation tool that announces the time and current weather conditions every hour on the hour. It features a system notification chime followed by a natural voice announcement.

## ✨ Features

* **Hourly Automation:** Uses `APScheduler` to trigger  at the top of every hour.
* **Live Weather:** Fetches real-time temperature and conditions for Columbus, OH, using `python-weather`.
* **Offline TTS:** Uses `pyttsx3` for instant text-to-speech without needing a cloud subscription.
* **Auditory Alert:** Plays a standard Windows system notification before speaking.

---

## 🛠️ Usage

### 1. Prerequisites

Ensure you have **Python 3.8+** installed. This script is optimized for Windows systems (e.g., your Predator Helios 300).

### 2. Install Libraries

Install the dependencies using `pip`:

```bash
pip install pyttsx3 python-weather apscheduler
```

### 3. Run the script

```bash
python main.py
```
