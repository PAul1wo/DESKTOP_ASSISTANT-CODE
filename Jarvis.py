import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import  get
import wikipedia
import webbrowser

import smtplib
import sys
import time
import pyjokes


import pyautogui





engine = pyttsx3.init('sapi5')          #text to voice
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[len(voices) - 1].id)


# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# To convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=8, phrase_time_limit=12)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query








def screenshot():
    pyautogui.keyDown("windows")
    pyautogui.press("Prtsc")
    pyautogui.keyUp("windows")



# to wish
def wish():
    hour = int(datetime.datetime.now().hour)  #Current time
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour <= 12:
        speak(f"good morning, its {tt}")
    elif hour >= 12 and hour <= 18:
        speak(f"good afternoon, its {tt}")
    else:
        speak(f"good evening, its {tt}")
    speak("i am jarvis sir. please tell me how may i help you")


# to send email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('YOUR EMAIL ADDRESS', 'YOUR PASSWORD')
    server.sendmail('YOUR EMAIL ADDRESS', to, content)
    server.close()


if __name__ == "__main__":  # main program
    wish()
    while True:
        # if 1:

        query = takecommand().lower()

        # logic building for tasks

        if "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)

        elif 'hi' in query or 'hello' in query:
            speak('Hello sir, how may I help you?')

        elif 'take screenshot' in query:
            screenshot()
            speak('Screenshot saved in pictures folder')

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)  # 0 for internal Camera
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()


        elif "play music" in query:
            speak('Yes , I can do that')
            music_dir = "D:\Musics"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))

        elif 'take a screenshot' in query:
            screenshot()


        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2,chars=10, auto_suggest=True, redirect=True)
            speak("according to wikipedia")
            speak(results)
            # print(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "search google" in query:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "close Facebook" in query:
            speak('Closing Facebook Now')
            os.system("taskkill /f /im chrome.exe")

        elif "calculator" or "calulate this for me" in query:
            speak('what operation you want to do')
            n = takecommand()
            if 'addition' or 'add' in n:
                speak('please , give me the two numbers ')
                n1 = takecommand()
                n2 = takecommand()
                add1 = int(n1) + int(n2)
                speak(f'your answer is {add1}')

            elif 'substraction' or 'substract' in n:
                speak('please , give me the two numbers ')
                n1 = takecommand()
                n2 = takecommand()
                sub1 = int(n1) - int(n2)
                speak(f'the answer is {sub1}')


        elif "close youtube" in query:
            speak('Closing youtube Now')
            os.system("taskkill /f /im chrome.exe")


        elif "close google" in query:
            speak('Closing google Now')
            os.system("taskkill /f /im chrome.exe")

        elif "close notepad" in query:
            speak('closing notepad')
            os.system("taskkill /f /im notepad.exe")

        elif "close cmd"  in query:
            speak('closing cmd')
            os.system("taskkill /f /im cmd.exe")

        elif "tell me a joke" or "can you tell me a joke" or "i want a joke" in query:
            speak('you want the joke , in which language')
            l = takecommand().lower()
            if "english" in l:
                joke = pyjokes.get_joke("en")
                speak(joke)
            elif "german" in l:
                joke = pyjokes.get_joke("de")
                speak(joke)

            elif "spanish" in l:
                joke = pyjokes.get_joke("es")
                speak(joke)


     #   elif "song on youtube" in query:
         #   kit.playonyt("see you again")

        elif 'timer' in query or 'stopwatch' in query:
            speak("For how many minutes?")
            timing = takecommand()
            timing = timing.replace('minutes', '')
            timing = timing.replace('minute', '')
            timing = timing.replace('for', '')
            timing = float(timing)
            timing = timing * 60
            speak(f'I will remind you in {timing} seconds')

            time.sleep(timing)
            speak(f'Your {timing} has been finished sir')


        elif "email to avinash" in query:
            try:
                speak("what should i say?")
                content = takecommand().lower()
                to = "EMAIL OF THE OTHER PERSON"
                sendEmail(to, content)
                speak("Email has been sent to avinash")

            except Exception as e:
                print(e)
                speak("sorry sir, i am not able to sent this mail to avi")

        elif "you can quit now" in query:
            speak("thanks for using me , have a good day.")
            sys.exit()

        #speak("Can I help with , with something else")
