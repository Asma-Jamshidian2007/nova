import speech_recognition as sr
import pyttsx3
import wikipedia
from datetime import datetime
import requests
import subprocess
import os
import psutil

engine = pyttsx3.init()
engine.setProperty('rate', 180)  
engine.setProperty('volume', 3.0) 
GEMINI_API_KEY = "AIzaSyCQcxy1rgvJmTHn7u5AeG_veXNyZwabStU"


def chat_with_ai(text):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

    headers = {"Content-Type": "application/json"}
    data = {"contents": [{"parts": [{"text": text}]}]}

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        return result["candidates"][0]["content"]["parts"][0]["text"]
    else:
        return "Sorry, I couldn't process your request."


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            command = recognizer.recognize_google(audio, language='en-US')
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that. Please say it again.")
            return None
        except sr.RequestError:
            speak("There was an issue connecting to the server.")
            return None
        except Exception as e:
            speak("An error occurred. Please try again.")
            print(e)
            return None


def open_application(app_name):
    try:
        subprocess.Popen(app_name, shell=True)
        speak(f"{app_name} has been opened.")
    except Exception as e:
        speak(f"An error occurred while trying to open {app_name}. Error: {str(e)}")


def close_application(app_name):
    for proc in psutil.process_iter(['pid', 'name']):
        if app_name.lower() in proc.info['name'].lower():
            try:
                proc.terminate()
                speak(f"{app_name} has been closed.")
            except Exception as e:
                speak(f"Sorry, I couldn't close {app_name}.")
                print(e)
            break
    else:
        speak(f"{app_name} is not running.")


def install_application(app_name):
    try:
        speak(f"Installing {app_name}, please wait...")
        subprocess.run(f"winget install {app_name}", shell=True)
        speak(f"{app_name} has been installed successfully.")
    except Exception as e:
        speak(f"Failed to install {app_name}. Error: {str(e)}")


def uninstall_application(app_name):
    try:
        speak(f"Uninstalling {app_name}, please wait...")
        subprocess.run(f"winget uninstall {app_name}", shell=True)
        speak(f"{app_name} has been removed successfully.")
    except Exception as e:
        speak(f"Failed to uninstall {app_name}. Error: {str(e)}")


def nova():
    speak("Hello! I am Nova, your assistant. How can I help you today?")
    while True:
        command = listen()
        if command:
            if 'hello' in command:
                speak("Hello! Hope you're doing well.")
            elif 'goodbye' in command or 'bye' in command:
                speak("Goodbye! Have a great day!")
                break
            elif 'wikipedia' in command:
                speak("Please tell me what you want to search.")
                query = listen()
                if query:
                    try:
                        summary = wikipedia.summary(query, sentences=2, auto_suggest=False, redirect=True)
                        speak("Here is what I found:")
                        speak(summary)
                    except wikipedia.DisambiguationError:
                        speak("Multiple topics found. Please be more specific.")
                    except wikipedia.PageError:
                        speak("I couldn't find anything. Please try again.")
            elif 'time' in command:
                now = datetime.now().strftime("%H:%M")
                speak(f"The current time is {now}.")
            elif 'open' in command:
                speak("What application would you like to open?")
                app = listen()
                if app:
                    open_application(app)
            elif 'close' in command:
                speak("What application would you like to close?")
                app = listen()
                if app:
                    close_application(app)
            elif 'install' in command:
                speak("What application would you like to install?")
                app = listen()
                if app:
                    install_application(app)
            elif 'uninstall' in command or 'remove' in command:
                speak("What application would you like to remove?")
                app = listen()
                if app:
                    uninstall_application(app)
            elif 'shutdown' in command or 'turn off' in command:
                speak("Shutting down the computer.")
                os.system("shutdown /s /t 1")
            else:
                response = chat_with_ai(command)
                speak(response)


if __name__ == "__main__":
    nova()
