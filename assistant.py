from datetime import datetime
import chitchat
from interface import Engine
import random
import dialogs


class Assistant:
    def __init__(self):
        self.engine = Engine()
        self.initialisation()


    def initialisation(self):
        chitchat.updateLogData('dataLog.txt')
        self.engine.speak("Initialisation de l'assistant")
        if chitchat.checkTimeBtw('dataLog.txt'):
            #checker si l'utiliateur est toujours le meme
            self.engine.speak(f"{dialogs.Salutation[random.randint(0, len(dialogs.Salutation-2))]} "
                              f"Monsieur, que puis-je faire pour vous")
        else:
            if int(str(datetime.now())[11:13])<17 :
                self.engine.speak('Bonjour')
            elif (int(str(datetime.now())[11:13]) > 17)and(int(str(datetime.now())[11:13]) < 24):
                self.engine.speak('Bonsoir')


