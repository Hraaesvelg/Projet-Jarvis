# seed the pseudorandom number generator
import random
from datetime import datetime
from transformers import pipeline

import dialogs


class Emotion:
    def __init__(self):
        self.probability = 0.5
        self.age = 0
        self.mood = 'Neutral'

    def update(self, proba):
        self.age += 1
        if proba == 'NONE':
            self.probability = self.probability
        else:
            self.probability = (self.probability + proba)/2

        if self.probability ==0.5 :
            self.mood = 'Neutral'
        elif self.probability<0.5:
            self.mood = 'Bad'
        elif self.probability>0.5:
            self.mood = 'Good'

    def getInfo(self):
        listInfo = [self.probability, self.mood, self.age]
        return listInfo


def chitChat(query, jarvis):
    if 'comment allez vous' or 'comment vas tu' or 'tu vas bien' in query:
        jarvis.engine.speak(dialogs.ReponseSante[random.randint(0, len(dialogs.ReponseSante)-1)])
    elif 'qui es tu' or 'appelles' in query:
        jarvis.engine.speak('je suis Jarvis')
    else:
        jarvis.engine.speak('none')


def eraseData(fichier):
    data = open(f'{fichier}', 'w')
    data.close

def updateLogData(fichier):
    fichierLec = open(f'{fichier}', "r")
    listLec = []
    for l in fichierLec:
        listLec.append(l)
    fichierLec.close()

    Nlist = []
    if len(listLec) >= 2:
        Nlist.append(listLec[len(listLec)-1])
        Nlist.append(str(datetime.now()))
    elif len(listLec) == 1:
        Nlist.append(listLec[len(listLec) - 1])
        Nlist.append(str(datetime.now()))
    elif len(listLec) == 0:
        Nlist.append(str(datetime.now()))
        Nlist.append(str(datetime.now()))

    eraseData("dataLog.txt")
    fichierEcr = open(f'{fichier}', "a")
    for date in Nlist:
        fichierEcr.write(date + '\n')
    fichierEcr.close()

def extractEmotion(query):
    classifier = pipeline("sentiment-analysis" )
    print(classifier(f'{query}',src_lang="fr_FR"))

def checkTimeBtw(fichier):
    fichierLec = open(f'{fichier}', "r")
    listLec = []
    for l in fichierLec:
        listLec.append(str(l))
    fichierLec.close()

    Nlist = []
    Nlist.append(listLec[0].split(' ')[1][0:7])
    Nlist.append(listLec[2].split(' ')[1][0:7])

    H1 = (int(Nlist[0].split(':')[0])*3600+int(Nlist[0].split(':')[1])*60+int(Nlist[0].split(':')[2]))/3600
    H2 = (int(Nlist[1].split(':')[0])*3600+int(Nlist[1].split(':')[1])*60+int(Nlist[1].split(':')[2]))/3600

    if abs(H1-H2) <= 1:
        return False
    else:
        return True

def faitMoiUneBlague():
    response = requests.get('https://www.blagues-api.fr/api/random', headers={
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNjkwNTc0ODAwODY3MDMzMjA4Iiwib'
                         'GltaXQiOjEwMCwia2V5IjoiWVZnWUFVYlJnYVoyYlo2dE1Tc1NzMXIxbVVhZ2xGM2hFWnVMUlprbXpTM3RHeWhINUQiL'
                         'CJjcmVhdGVkX2F0IjoiMjAyMS0wNC0xM1QxNjozODo0NSswMDowMCIsImlhdCI6MTYxODMzMTkyNX0.vsf6Nlkm-B0XsU'
                         'JAP-ePO7gg_ucwZxIisXgUrvySxOs'})
    data = response.json()
    return [data['joke'], data['answer']]
