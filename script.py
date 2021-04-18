import pyttsx3
import datetime
import time
import speech_recognition as sr
import wikipedia
import pywhatkit
import webbrowser
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
import keyword

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 180)
# setting up chrome
chrome = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greet():
    hour = int(datetime.datetime.now().hour)
    if hour <= 0 and hour < 12:
        speak("Good morning Jagrav!")
    elif hour >= 12 and hour <= 18:
        speak("Good evening Tapu sena !")
    else:
        speak("Have a good sleep !")

    speak("I am friday, your friendly assistant. How may I help you ? ")


def take_commands():

    # takes speech input and returns output as a string

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User : {query}\n")
    except:
        speak("Sorry, I didn't get it")
        print("Try agian ")
        return "None"
    return query


if __name__ == '__main__':
    # greet()
    # driver = webdriver.Chrome("chromedriver.exe")
    while True:
        # if 1:
        query = take_commands().lower()

        # Logic for executing tasks
        if "wikipedia" in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("As per wikipedia")
            print(results)
            speak(results)
        elif 'stop' in query:
            speak("Stoping...")
            exit()

            # DISCRETE MATHEMATICS (bmp)
        elif 'open discrete mathematics b' in query:
            speak("Joining class for discrete mathematics")
            webbrowser.get(chrome).open(
                "https://meet.google.com/tfq-enjd-wga?pli=1&authuser=2")
            time.sleep(3)
            pyautogui.hotkey('ctrl', 'e')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'd')
            time.sleep(2)
            pyautogui.click(1346, 603)
            pyautogui.sleep(5)

        #   OPERATING SYSTEM( lab )
        elif 'open os lab' in query:
            speak("Joining lab for Operating System")
            webbrowser.get(chrome).open(
                "https://meet.google.com/sre-kbtx-fvw?pli=1&authuser=2")
            time.sleep(3)
            pyautogui.hotkey('ctrl', 'e')
            time.sleep(2)
            pyautogui.hotkey('ctrl', 'd')
            time.sleep(2)
            pyautogui.click(1346, 603)
            pyautogui.sleep(5)

        # COA (neha)
        elif 'open Computer Organisation Neha' in query:
            speak("Joining class for Computer Organization Architecture")
            webbrowser.get(chrome).open(
                "https://meet.google.com/jhq-wfya-zrr?pli=1&authuser=2")
            time.sleep(3)
            pyautogui.hotkey('ctrl', 'e')
            time.sleep(2)
            pyautogui.hotkey('ctrl', 'd')
            time.sleep(2)
            pyautogui.click(1346, 603)
            pyautogui.sleep(5)

        #  DM (hrp-harshad)

        elif 'open dm harshad' in query:
            speak("Joining class for Discrete Mathematics")
            webbrowser.get(chrome).open(
                "https://meet.google.com/vnh-mskx-wri?pli=1&authuser=2")
            time.sleep(3)
            pyautogui.hotkey('ctrl', 'e')
            time.sleep(2)
            pyautogui.hotkey('ctrl', 'd')
            time.sleep(2)
            pyautogui.click(1346, 603)
            pyautogui.sleep(5)

        elif 'open os rimi' in query:
            speak("Joining class for Discrete Mathematics")
            webbrowser.get(chrome).open(
                "https://meet.google.com/xzr-uoyp-zcf?pli=1&authuser=2")
            time.sleep(3)
            pyautogui.hotkey('ctrl', 'e')
            time.sleep(2)
            pyautogui.hotkey('ctrl', 'd')
            time.sleep(2)
            pyautogui.click(1346, 603)
            pyautogui.sleep(5)
