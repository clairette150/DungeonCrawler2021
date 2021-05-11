from model.Items.Item import Item

class AttackItem(Item):
    #TODO: Extend
    def __init__(self, id=0, name="nothing", desc="", useable=False, equipable=False, quality=0, dmg=0):
        super().__init__(id, name, desc, useable, equipable, quality)
        self.__dmg = dmg

    # Returns if the item damage value.
    def getDamage(self):
        return self.__dmg