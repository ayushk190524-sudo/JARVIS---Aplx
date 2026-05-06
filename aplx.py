import os
import subprocess #this is important for the code to use facts of the system
import shutil
import time
import webbrowser
from datetime import datetime
import sys #this is used for the aplx to know time and date

def speak(text, delay=0.04):
    """Displays text letter by letter for that ChatGPT/Jarvis feel."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
    

def open_default_browser(url=None):
    try:
        target = url if url else "https://www.google.com"
        if shutil.which("xdg-open"):
            subprocess.Popen(["xdg-open", target], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
        elif shutil.which("gio"):
            subprocess.Popen(["gio", "open", target], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
        else:
            webbrowser.open(target)
    except Exception as err:
        speak(f"Unable to open browser: {err}")


def open_file_explorer():
    try:
        if shutil.which("gio"):
            subprocess.Popen(["gio", "open", "."], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
        elif shutil.which("xdg-open"):
            subprocess.Popen(["xdg-open", "."], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
        else:
            speak("No file explorer command is available on this system.")
    except Exception as err:
        speak(f"Could not open file explorer: {err}")


def greet_me():
    user = os.environ.get('USER', 'R3nz')
    hour = datetime.now().hour

    if hour < 12:
        greet = "Good morning, R3nz"
    elif 12 <= hour < 18:
        greet = "Good afternoon, R3nz"
    else:
        greet = "Good evening, R3nz"

    speak(f"--- {greet}, {user}, Aplx AI is online.---")
greet_me()

while True:
    #so this is the command box next to the Aplx AI, you can type your commands here
    try:
        query = input("What can I do for you, R3nz? >> ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        speak("Input interrupted. Type 'exit' or 'sleep' if you want to close the program.")
        continue

    if not query:
        continue

    try:
        if "exit" in query or "sleep" in query:
            speak("System powering down, Goodbye for now, R3nz.")
            break

        elif "time" in query:
            now = datetime.now().strftime("%I:%M:%S %p")
            speak(f"The current time is {now}.")
        elif "battery" in query or "btry" in query or "battry" in query:
            if os.path.exists('/sys/class/power_supply/BAT0/capacity'):
                with open('/sys/class/power_supply/BAT0/capacity', 'r') as f:
                    percentage = f.read().strip()
                speak(f"Current Power percentage: {percentage}%")
            else:
                speak("Battery information not available.")
        elif "browser" in query or "internet" in query:
            speak("Opening your default web browser...")
            open_default_browser()
        elif "file" in query or "folder" in query:
            speak("Opening your file explorer...")
            open_file_explorer()
        elif "youtube" in query:
            speak("Opening YouTube...")
            open_default_browser("https://www.youtube.com")
        elif "roblox" in query or "sober" in query:
            speak("Opening Roblox website...")
            open_default_browser("https://www.roblox.com")
        elif "nerd app" in query or "mission jeet" in query or "hell" in query:
            speak("Opening Mission Jeet (or, nerd app as you say)...")
            open_default_browser("https://missionjeet.in/")
        elif "shop" in query or "amazon" in query:
            speak("Opening Amazon...")
            open_default_browser("https://www.amazon.in/")
        elif "government" in query:
            speak("Opening government website...")
            open_default_browser("https://www.MyGov.in/")
        elif "idk what to say" in query or "idk what to do" in query:
            speak("Just ask me to open something, R3nz. I can open your browser, file explorer, and even specific websites like YouTube, Roblox, and Amazon.")
        elif "github" in query or "code" in query or "my app" in query:
            speak("Opening GitHub...")
            open_default_browser("https://github.com")
        elif "help" in query or "commands" in query or "/help" in query:
            speak("Here are some commands you can try:")
            speak("- 'time' to know the current time")
            speak("- 'battery' to check battery percentage")
            speak("- 'browser' or 'internet' to open your default web browser")
            speak("- 'file' or 'folder' to open your file explorer")
            speak("- 'youtube' to open YouTube")
            speak("- 'roblox' or 'sober' to open the Roblox website")
            speak("- 'nerd app' or 'mission jeet' to open the Mission Jeet website")
            speak("- 'shop' or 'amazon' to open Amazon")
            speak("- 'government' to open the government website")
            speak("- 'weather' to open the weather forecast")
            speak("- 'money eater' or 'pocket filled fatty' or 'a dumbass' to open their respective websites")
            speak("- 'github' or 'code' or 'my app' to open GitHub")
            speak("- I can also enable study mode automatically on week days from 4:10 PM to 6:10 PM as per due to tution")
        elif "sup dumbass" in query or "sup idiot" in query:
            speak("Wsg loser, What you want now?.") 
        elif "weather" in query:
            speak("Opening weather forecast...")
            open_default_browser("Put your city weather here")
        elif "money eater" in query or "pocket filled fatty" in query or "a dumbass" in query:
            speak("Opening A (not so) great womans wiki...")
            open_default_browser("https://en.wikipedia.org/wiki/Nirmala_Sitharaman")
    except Exception as err:
        speak(f"An error occurred handling that command: {err}")
        continue
    




