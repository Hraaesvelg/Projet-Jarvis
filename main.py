import subprocess
import wolframalpha
import tkinter
import json
import operator
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
#from client.textui import progress
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen


import chitchat
import dialogs
import random
from assistant import Assistant




#------Main--------#

Jarvis = Assistant()
while True:

    query = Jarvis.engine.takeCommand().lower()

    if 'stop' or 'pause' in query:
        if 'stop' in query:
            Jarvis.engine.speak('Tres bien, je termine les processus')
            Jarvis.engine.speak(dialogs.Aurevoir[random.randint(0, len(dialogs.Aurevoir)-1)])
            exit()

        elif 'pause' in query:
            Jarvis.engine.speak('Tres bien, je me met en pause, pressez une touche pour me reveiller')
            Jarvis.engine.speak(dialogs.Aurevoir[random.randint(0, len(dialogs.Aurevoir) - 1)])
            programPause = input("Pressez une touche ...")
            Jarvis.engine.speak(dialogs.Salutation[random.randint(0, len(dialogs.Salutation) - 2)])

    if 'wikipedia' in query:
        Jarvis.engine.speak('Je cherche sur Wikipédia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=3)
        Jarvis.engine.speak("Selon wikipedia")
        Jarvis.engine.speak(results)

    elif 'ouvre youtube' in query:
        Jarvis.engine.speak("Voilà Youtube\n")
        webbrowser.open("youtube.com")

    elif 'ouvre google' in query:
        Jarvis.engine.speak('Souhaitez vous cherchez quelque-chose de particulier')
        answer = Jarvis.engine.takeCommand().lower()
        if 'oui' in answer:
            Jarvis.engine.speak('Sur quel sujet ?')
            commande = Jarvis.engine.takeCommand()
            webbrowser.open(commande)
        elif 'non' in answer:
            Jarvis.engine.speak("Et voici Google\n")
            webbrowser.open("google.com")

    elif 'ouvre stackoverflow' in query:
        Jarvis.engine.speak("Stackoverflow est ouvert. Bonne programmation ")
        webbrowser.open("stackoverflow.com")

    elif 'met de la musique' in query or "met une chanson" in query or "deezer" in query :
        #ici mettre de la musique
        pass

    elif 'heure' in query:
        strTime = str(datetime.datetime.now())
        Jarvis.engine.speak(f"Il est actuelement {strTime[11:13]} heure {strTime[14:16]}")


    elif 'send a mail' in query:
        try:
            Jarvis.engine.speak("What should I say?")
            content = Jarvis.engine.takeCommand()
            Jarvis.engine.speak("whome should i send")
            to = input()
            sendEmail(to, content)
            Jarvis.engine.speak("Email has been sent !")
        except Exception as e:
            print(e)
            Jarvis.engine.speak("I am not able to send this email")

    elif 'comment vas tu' in query:
        Jarvis.engine.speak(dialogs.ReponseSante[random.randint(0, len(dialogs.ReponseSante)-1)])
        #mettre de la response

    elif "quel est ton nom" in query or "comment t'appeles tu" in query:
        Jarvis.engine.speak("Je m'appelle Jarvis et je suis la pour vous aider")


    elif "Qui t'as créé" in query or "qui t'a fait" in query:
        Jarvis.engine.speak("J'ai été créé par notre maitre à tous, Valentin.")

    elif 'blaques' in query:
        blague = chitchat.faitMoiUneBlague()
        Jarvis.engine.speak(blague[0])
        Jarvis.engine.speak(blague[1])

    elif "calcule" in query:

        app_id = "Wolframalpha api id"
        client = wolframalpha.Client(app_id)
        indx = query.lower().split().index('calcule')
        query = query.split()[indx + 1:]
        res = client.query(' '.join(query))
        answer = next(res.results).text
        Jarvis.engine.speak("La réponse est " + answer)




    elif 'news' in query:

        try:
            jsonObj = urlopen(
                '''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
            data = json.load(jsonObj)
            i = 1

            speak('here are some top news from the times of india')
            print('''=============== TIMES OF INDIA ============''' + '\n')

            for item in data['articles']:
                print(str(i) + '. ' + item['title'] + '\n')
                print(item['description'] + '\n')
                speak(str(i) + '. ' + item['title'] + '\n')
                i += 1
        except Exception as e:

            print(str(e))


    elif 'lock window' in query:
        speak("locking the device")
        ctypes.windll.user32.LockWorkStation()

    elif 'shutdown system' in query:
        speak("Hold On a Sec ! Your system is on its way to shut down")
        subprocess.call('shutdown / p /f')

    elif 'empty recycle bin' in query:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
        speak("Recycle Bin Recycled")

    elif "don't listen" in query or "stop listening" in query:
        speak("for how much time you want to stop jarvis from listening commands")
        a = int(takeCommand())
        time.sleep(a)
        print(a)

    elif "where is" in query:
        query = query.replace("where is", "")
        location = query
        speak("User asked to Locate")
        speak(location)
        webbrowser.open("https://www.google.nl / maps / place/" + location + "")

    elif "camera" in query or "take a photo" in query:
        ec.capture(0, "Jarvis Camera ", "img.jpg")

    elif "restart" in query:
        subprocess.call(["shutdown", "/r"])

    elif "hibernate" in query or "sleep" in query:
        speak("Hibernating")
        subprocess.call("shutdown / h")

    elif "log off" in query or "sign out" in query:
        speak("Make sure all the application are closed before sign-out")
        time.sleep(5)
        subprocess.call(["shutdown", "/l"])

    elif "write a note" in query:
        speak("What should i write, sir")
        note = takeCommand()
        file = open('jarvis.txt', 'w')
        speak("Sir, Should i include date and time")
        snfm = takeCommand()
        if 'yes' in snfm or 'sure' in snfm:
            strTime = datetime.datetime.now().strftime("% H:% M:% S")
            file.write(strTime)
            file.write(" :- ")
            file.write(note)
        else:
            file.write(note)

    elif "show note" in query:
        speak("Showing Notes")
        file = open("jarvis.txt", "r")
        print(file.read())
        speak(file.read(6))

    elif "weather" in query:

        # Google Open weather website
        # to get API of Open weather
        api_key = "Api key"
        base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
        speak(" City name ")
        print("City name : ")
        city_name = takeCommand()
        complete_url = base_url + "appid =" + api_key + "&q =" + city_name
        response = requests.get(complete_url)
        x = response.json()

        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            print(" Temperature (in kelvin unit) = " + str(
                current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(
                current_pressure) + "\n humidity (in percentage) = " + str(
                current_humidiy) + "\n description = " + str(weather_description))

        else:
            speak(" City Not Found ")

