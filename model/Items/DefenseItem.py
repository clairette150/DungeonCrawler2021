from model.Items.Item import Item

class DefenseItem(Item):
    def __init__(self, id=0, name="nothing", desc="", useable=False, equipable=False, quality=0, icon="i", defense=0, ingL=[]):
        super().__init__(id, name, desc, useable, equipable, quality,icon,ingL)
        self.__defense = defense

    # Returns if the item defense value.
    def getDefense(self):
        return self.__defense
