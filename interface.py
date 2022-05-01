import pyttsx3
import speech_recognition as sr
import chitchat

class Engine:
    def __init__(self):
        self.engine = pyttsx3.init('sapi5')
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[0].id)
        self.emotion = chitchat.Emotion()
        self.formerInteraction = 'None'

        self.entryMode = 'Dev'
        print(f"'Initialisation : mode --> ' {self.getEntryMode()}")

    def speak(self, audio):
        self.formerInteraction = audio
        if self.entryMode == 'Dev':
            print(audio)
            chitchat.updateLogData('dataLog.txt')
        elif self.entryMode == 'User':
            self.engine.say(audio)
            self.engine.runAndWait()
            chitchat.updateLogData('dataLog.txt')
    def takeCommand(self):
        if self.entryMode == 'Dev':
            query = input('Entrez votre commande : ')
            return query
        elif self.entryMode == 'User':
            r = sr.Recognizer()
            with sr.Microphone() as source:

                print("Listening...")
                r.pause_threshold = 1
                audio = r.listen(source)

            try:
                print("Recognizing...")
                query = r.recognize_google(audio, language='fr-FR')
                print(f"User said: {query}\n")

            except Exception as e:
                print(e)
                print("Unable to Recognize your voice.")
                return "None"

            return query


    def changeEntryMode(self):
        if self.entryMode == 'Dev':
            self.entryMode = 'User'
        elif self.entryMode == 'User':
            self.entryMode = 'Dev'
        else:
            self.entryMode = 'Dev'

    def getEntryMode(self):
        return self.entryMode


