from abc import ABC

class AbstractObject(ABC):
    def __init__(self, name=""):
        self.__name = name

    #Returns the name of the object
    def getName(self):
        return self.__name
