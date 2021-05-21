import pyttsx3
import speech_recognition as sr
import datetime
import winshell
import pytesseract
import os
import pyperclip
from googletrans import Translator
import cv2
import random
import instalooter
from requests import  get
import wikipedia
import webbrowser
import requests
import smtplib
import sys
import time
import pyjokes
import pyautogui
import json
import geocoder
import pyautogui
import wolframalpha
import PyPDF2


g = geocoder.ip('me')

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


def readfile():
    t = open("a.txt","r")
    r = t.read()
    speak(r)
    t.close()

def pdf_reader():
    book = open('Data Structures and Algorithms Made Easy_ Data Structures and Algorithmic Puzzles ( PDFDrive ).pdf','rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f'Total Number of Pages in this book is {pages}')
    speak('enter the page number i have to read')
    pg = int(input('Please Enter the page Number : '))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)

def locate():
    place=query[1]
    speak(f"according to my data base {place} lies here")
    webbrowser.open_new_tab("https://www.google.com/maps/place/"+place)


def weather(): #for Weather, Location , Lattitude, Longitude, Humidity, temperature
    api_url = "https://fcc-weather-api.glitch.me/api/current?lat=" + \
        str(g.latlng[0]) + "&lon=" + str(g.latlng[1])

    data = requests.get(api_url)
    data_json = data.json()
    if data_json['cod'] == 200:
        main = data_json['main']
        wind = data_json['wind']
        weather_desc = data_json['weather'][0]
        speak(str(data_json['coord']['lat']) + 'latitude' + str(data_json['coord']['lon']) + 'longitude')
        speak('Current location is ' + data_json['name'] + data_json['sys']['country'] + 'dia')
        speak('weather type ' + weather_desc['main'])
        speak('Wind speed is ' + str(wind['speed']) + ' metre per second')
        speak('Temperature: ' + str(main['temp']) + 'degree celcius')
        speak('Humidity is ' + str(main['humidity']))

def news():
    api_url1 = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=f439165f85a3440c84b7f0d1552e2c32"

    page = requests.get(api_url1).json()  # we scrap the Data from the Url by json and put the data in the variable page
    articles = page["articles"]  # Only taking the Articles from the page.
    head = []
    day = ["first","second","third","fourth","fifth"]
    for ar in articles:
        head.append(ar["title"]) #Fro Articles we take only the titles.
    for i in range(len(day)):
        speak(f"today's {day[i]} , your latest news are :{head[i]}")
    speak("that were today's five latest news, hope they were informative")


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
    speak("i am a Desktop Assistant. please tell me how may i help you")


def langtranslator():
    try:
        trans = Translator()

        speak("Say the language to translate in")
        language = takecommand().replace(" ", "")

        speak("what to translate")
        content = takecommand()

        t = trans.translate(text=content, dest=language)
        print(f"{t.origin} in {t.dest} is , {t.text}")

    except:
        speak("error")


# to send email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    email = "sasangkasarma7@gmail.com"
    password = input()
    server.login(email, password)
    send_email = input()
    server.sendmail(send_email, to, content)
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

        if "where is" in query:
            query = query.split("where is")
            locate()

        elif 'can you remember this' in query:
            speak("what should i remember sir")
            rememberMessage = takecommand()
            speak(f"you said me to remember {rememberMessage}")
            remember = open('data.txt', 'w')
            remember.write(rememberMessage)
            remember.close()

        if "translate to" in query:
            text = query.split("translate to")
            dest = text[1]
            langtranslator()


        if "where am i" in query or "what is my location now" in query:
            speak('please wait, i am checking')
            try:
                ipadd = requests.get('https://api.ipify.org').text
                #print(ipadd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipadd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                country = geo_data['country']
                speak(f'i am not sure but i think we are in {city} in {country} country')

            except Exception as e:
                speak('Sorry')
                pass

        elif 'read book' in query:
            pdf_reader()


        elif "instagram profile" in query or "profile on instagram" in query:
            speak('please, enter the instagram username correctly')
            name = input('Enter the Username here : ')
            webbrowser.open(f'www.instagram.com/{name}')
            speak(f'here is the Profile with username {name}')
            time.sleep(5)
            speak('would you like to download profile picture of this account ')
            condition = takecommand().lower()
            if "yes" in condition:
                mod = instalooter.Instaloader()   #Error here!
                mod.download_profile(name,profile_pic_only=True)
                speak('i am done')
            else:
                pass




        elif 'do you remember anything' in query:
            remember = open('data.txt', 'r')
            t = remember.read()
            speak(f"you said me to remember that {t}")
            remember.close()

        
        elif "screenshot" in query or "take screenshot" in query:  #Working fine
            speak('please , tell me the name you want for the screenshot file')
            name = takecommand().lower()
            speak('hold on , taking screenshot')
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak('screenshot is saved in our main folder , please check')


        elif "bones" in query:
            speak('206 , that was easy')

        elif "open command prompt" in query or "open CMD" in query:
            os.system("start cmd")

        elif "open camera" in query or "open webcam" in query:
            cap = cv2.VideoCapture(0)  # 0 for internal Camera
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()




        elif "weather" in query:
            weather()

        elif "tell me latest news" in query:
            news()




        elif "switch window please" in query:
            speak('Switching to Previous Window')
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")


        elif "play music" in query:
            speak('Yes , I can do that')
            music_dir = "D:\\Musics"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))

        elif 'read a file' in query:
            readfile()

        elif 'how are you' in query or 'how are you doing' in query:
            speak("am fine , what about you?")
            query = takecommand()
            if 'am also good' in query or 'am also fine' in query or 'healthy' in query or 'fine' in query:
                speak("wow")
            if 'not well' in query or 'not good' in query or 'felling low' in query or 'not in mood' in query:
                speak("sad to hear that sir, how may I change your mood, May i play music for You?")
                query = takecommand()
                if 'ok' in query or 'sure' in query or 'hmm' in query or 'alright' in query or 'yeah' in query or 'play music' in query:
                    speak('ok , playing music for you')
                    music_dir = 'D:\\Musics'
                    songs = os.listdir(music_dir)   # Error Here
                    rd = random.choice(songs)
                    print(songs)
                    for songs in songs:
                        if songs.endswith('.mp3'):
                            os.startfile(os.path.join(music_dir, songs))
                elif "no" in query or "it's ok" in query or "don't play" in query or 'nope' in query:
                    speak("Ok , as You like!")


        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1,chars=10, auto_suggest=True, redirect=True)
            speak("according to wikipedia")
            speak(results)
            # print(results)

        elif 'what is the time' in query:
            hour = int(datetime.datetime.now().hour)  # Current time
            tt = time.strftime("%I:%M %p")
            speak(f'its {tt}')

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

        elif  "can you tell me a joke"  in query or "tell me a joke" in query or "i am sad tell a joke" in query:
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


        elif "email" in query:
            try:
                speak("what should i say?")
                content = takecommand().lower()
                to = "EMAIL OF THE OTHER PERSON"
                sendEmail(to, content)
                speak("Email has been sent")

            except Exception as e:
                print(e)
                speak("sorry , i am not able to sent this mail ")

        elif "you can quit now" in query or "quit" in query or "goodbye" in query:
            speak("thanks for using me ")
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 18:
                speak("Have a Nice day !")
                exit()
            elif hour >= 18 and hour < 24:
                speak("good Night ")

            sys.exit()

        #speak("Can I help with , with something else")
