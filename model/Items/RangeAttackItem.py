from model.Items.AttackItem import AttackItem

class RangeAttackItem(AttackItem):
    def __init__(self, id=0, name="nothing", desc="", useable=False, equipable=False, quality=0, icon="i", ingL=[], dmg=0, speed=0, range=0):
        super().__init__(id, name, desc, useable, equipable, quality,icon, ingL, dmg)
        self.__range = range
        self.__speed = speed

    # Returns the item damage value.
    def getDamage(self):
        return self.__dmg

    # Returns the speed of the ranged weapon
    def getSpeed(self):
        return self.__speed

    #Returns the range of the ranged weapon
    def getRange(self):
        return self.__speed
