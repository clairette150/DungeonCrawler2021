from model.Items.Item import Item

class DefenseItem(Item):
    # TODO: Extend
    def __init__(self, id=0, name="nothing", desc="", useable=False, equipable=False, quality=0, defense=0):
        super().__init__(id, name, desc, useable, equipable, quality)
        self.__defense = defense

    # Returns if the item defense value.
    def getDefense(self):
        return self.__defense