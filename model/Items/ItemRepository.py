import json
from model.Items.Item import Item
from model.Items.AttackItem import AttackItem
from model.Items.RangeAttackItem import RangeAttackItem
from model.Items.DefenseItem import DefenseItem
from model.Items.UseItem import UseItem
import ast 

class ItemRepository:
    def __init__(self, pathItem="", pathAttackItem="", pathRangeAttackItem="", pathDefenseItem="", pathUseItem=""):
        self.__itemList =  {}
        self.applyTo(pathItem, self.castToItem)
        self.applyTo(pathAttackItem, self.castToAttackItem)
        self.applyTo(pathRangeAttackItem, self.castToRangeAttackItem)
        self.applyTo(pathDefenseItem, self.castToDefenseItem)
        self.applyTo(pathUseItem, self.castToUseItem)
        
    #Reads predefined items from a json file
    def applyTo(self, file, function):
        if file == "":
            return
        with open(file) as json_file:
            data = json.load(json_file)
            for entry in data:
                    currentItem = function(entry)
                    self.__itemList[currentItem.getItemId()] = currentItem

    #Returns Item from dict.
    def castToItem(self, l):
        id = l["id"]
        name = l["name"]
        desc = l["desc"]
        useable = l["useable"]
        equipable = l["equipable"]
        quality = l["quality"]
        icon = l["icon"]
        ingL = l["ingL"]
        return Item(id, name, desc, useable, equipable, quality, icon, ingL)

    #Returns AttackItem from dict.
    def castToAttackItem(self, l):
        id = l["id"]
        name = l["name"]
        name = l["name"]
        desc = l["desc"]
        useable = l["useable"]
        equipable = l["equipable"]
        quality = l["quality"]
        icon = l["icon"]
        ingL = l["ingL"]
        desc = l["desc"]
        useable = l["useable"]
        equipable = l["equipable"]
        quality = l["quality"]
        icon = l["icon"]
        ingL = l["ingL"]
        dmg = l["dmg"]
        return AttackItem(id, name, desc, useable, equipable, quality, icon, ingL, dmg)
    
    #Return RangeAttackItem form dict.
    def castToRangeAttackItem(self, l):
        id = l["id"]
        name = l["name"]
        desc = l["desc"]
        useable = l["useable"]
        equipable = l["equipable"]
        quality = l["quality"]
        icon = l["icon"]
        ingL = l["ingL"]
        dmg = l["dmg"]
        speed = l["speed"]
        range = l["range"]
        return RangeAttackItem(id, name, desc, useable, equipable, quality, icon, ingL, dmg , speed, range)

    #Returns DefenseItem from dict.
    def castToDefenseItem(self, l):
        id = l["id"]
        name = l["name"]
        desc = l["desc"]
        useable = l["useable"]
        equipable = l["equipable"]
        quality = l["quality"]
        icon = l["icon"]
        ingL = l["ingL"]
        defense = l["defense"]
        return DefenseItem(id, name, desc, useable, equipable, quality, icon, ingL, defense)

    #Returns UseItem from dict.
    def castToUseItem(self, l):
        id = l["id"]
        name = l["name"]
        desc = l["desc"]
        useable = l["useable"]
        equipable = l["equipable"]
        quality = l["quality"]
        icon = l["icon"]
        ingL = l["ingL"]
        #TODO: handle use function here?
        return UseItem(id, name, desc, useable, equipable, quality, icon, ingL)
    
    #Returns the current item list/dict.
    def getItemList(self):
        return self.__itemList
   
    #Loads a custom item from a dict
    def loadCustomItem(self, inputItemDict):
        inputItemDict = ast.literal_eval(inputItemDict)
        iType = inputItemDict["type"]
        if iType == "Item":
            return self.castToItem(inputItemDict)
        elif(iType == "AttackItem"):
            return self.castToAttackItem(inputItemDict)
        elif(iType == "DefenseItem"):
            return self.castToDefenseItem(inputItemDict)
        elif(iType == "UseItem"):
            return self.castToUseItem(inputItemDict)
        elif(iType =="RangeAttackItem"):
            return self.castToRangeAttackItem(inputItemDict)