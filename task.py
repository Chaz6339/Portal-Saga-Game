class Task:
    def __init__(self, name):
        self._name = name
        self._dictionary = {}

    def addComponent(self, number, componentName):
        self._dictionary[componentName] = number

    def getName(self):
        return self._name

    def getComponents(self):
        return self._dictionary