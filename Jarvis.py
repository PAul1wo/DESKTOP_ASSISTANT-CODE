import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random


engine = pyttsx3.init('sapi5') #text to voice
voices = engine.getProperty('voices')
engine.setProperty('voices' , voices[0].id)


def speak(audio):   #text - > speech
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def take_commnad(): #Voice - > text

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold  = 1  # Program won't stop Until 1 second
        audio = r.listen(source,timeout=8,phrase_time_limit=12)

    try:
        print("Recognizing............")
        query = r.recognize_google(audio,language = 'en-in')
        print(f"User Said!:{query}")

    except Exception as e:
        speak("Sorry I did Not get it Please Say that again...")
        return "none"
    return query

def wishing():
    hour = int(datetime.datetime.now().hour)

    if hour >=0 and hour <=12:
        speak("good morning")
    elif hour >12 and hour <=18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak('Hope Your Safe and Sound . How Can i help you')

if __name__ == "__main__":
    wishing()
    while True:

        query = take_commnad().lower() # user input storing in Query

        #logic building for Tasks

        if "open notepad" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif "open command prompt" in query:
            cpath = "C:\\WINDOWS\\system32\\cmd.exe"
            os.startfile(cpath)

        elif "open camera" in query: #Open Camera
            cap = cv2.VideoCapture(0) # 0 -> for internal Camera
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(30)
                if k==20:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query: # Play Music
            music_dir = "D:\\Musics"
            songs = os.listdir(music_dir)  # music converted into a list
            rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))

