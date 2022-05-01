

class calendar:
    def __init__(self):
        self.listActivity = []
        self.engine = Engine()

    def addActivity(self):
        self.activity = Activity()
        self.engine.speak("Nous allons commencer la création d'une nouvelle activité")


class Activity:
    def __init__(self):
        self.begin
        self.end
        self.hDuration
        self.name
        self.location
        self.category
        self.id
        self.description
        self.date
        self.frequency
        self.numberLeft

    def setBegin(self, value):
        self.begin = value

    def setEnd(self, value):
        self.end = value
    def setHDuration(self, value):
        self.hDuration= value
    def setName(self, value):
        self.name = value
    def setLocation(self, value):
        self.location = value
    def setCategory(self, value):
        self.category = value
    def setId(self, value):
        self.id = value
    def setDescription(self, value):
        self.description = value
    def setDate(self, value):
        self.date = value
    def setFrequency(self, value):
        self.frequency = value
    def setNumberLeft(self, value):
        self.numberLeft = value

    def getInfo(self):
        listInfo = [self.begin,self.end, self.hDuration,self.name, self.location,
                    self.category, self.id, self.description, self.date, self.frequency,
                    self.numberLeft ]
        return listInfo