import json
from model.Items.Item import Item
from model.Items.AttackItem import AttackItem
from model.Items.RangeAttackItem import RangeAttackItem
from model.Items.DefenseItem import DefenseItem
from model.Items.UseItem import UseItem

class ItemRepository:
    def __init__(self, pathItem="", pathAttackItem="", pathRangeAttackItem="", pathDefenseItem="", pathUseItem=""):
        self.__itemList =  {}
        self.applyTo(pathItem, self.castToItem)
        self.applyTo(pathAttackItem, self.castToAttackItem)
        self.applyTo(pathRangeAttackItem, self.castToRangeAttackItem)
        self.applyTo(pathDefenseItem, self.castToDefenseItem)
        self.applyTo(pathUseItem, self.castToUseItem)

    def applyTo(self, file, function):
        if file == "":
            return
        with open(file) as json_file:
            data = json.load(json_file)
            for entry in data:
                    currentItem = function(entry)
                    self.__itemList[currentItem.getItemId()] = currentItem

    #Returns Item form json.
    def castToItem(self, line):
        id, name, desc, useable, equipable, quality, icon, ignL = line
        return Item(id, name, desc, useable, equipable, quality, icon, ignL)
    #Returns AttackItem from json.
    def castToAttackItem(self, line):
        id, name, desc, useable, equipable, quality, icon, ignL,dmg = line
        return AttackItem(id, name, desc, useable, equipable, quality, icon, ignL, dmg)
    #Return RangeAttackItem form json.
    def castToRangeAttackItem(self, line):
        id, name, desc, useable, equipable, quality, icon, ignL, dmg , speed, range = line
        return RangeAttackItem(id, name, desc, useable, equipable, quality, icon, ignL, dmg , speed, range)
    #Returns DefenseItem from json.
    def castToDefenseItem(self, line):
        id, name, desc, useable, equipable, quality, icon, ignL, defense = line
        return DefenseItem(id, name, desc, useable, equipable, quality, icon, ignL, defense)
    #Returns UseItem from json.
    def castToUseItem(self, line):
        id, name, desc, useable, equipable, quality, icon, ignL = line
        return UseItem(id, name, desc, useable, equipable, quality, icon, ignL)
    #Returns the current item list/dict.
    def getItemList(self):
        return self.__itemList
