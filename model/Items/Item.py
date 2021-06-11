from model.AbstractObject import AbstractObject
class Item(AbstractObject):
    # Creates an item where:
    # id(default:0) is the item id
    # name(default:"") is the name of the item.
    # desc(default:"") is the description of the item.
    # useable(default: False) is the item useable?
    # equipable(default:False) is the item equipable?
    # quality(default:0) is the quality of the item.
    # Icon is an icon or a sprite for the Item
    # ingL is the ingredients list for crafting the item
    def __init__(self, id=0, name="", desc="", useable=False, equipable=False, quality=0, icon="i", ingL=[]):
        super().__init__(name)
        self.__id = id
        self.__desc = desc
        self.__useable = useable
        self.__equipable = equipable
        self.__quality = quality
        self.__icon = icon
        self.__ingL = ingL
        self.__type = type(self).__name__

    # Returns item id.
    def getItemId(self):
        return self.__id

    # Returns item description.
    def getDescription(self):
        return self.__desc

    # Returns if the item is equipable.
    def isEquipable(self):
        return self.__equipable

    # Returns if the item is useable.
    def isUseable(self):
        return self.__useable

    # Returns the item quality.
    def getQuality(self):
        return self.__quality

    # Sets the item quality.
    def setQuality(self, quality):
        self.__quality = quality

    #Returns the icon of the item
    def getIcon(self):
        return self.__icon
    #Returns the ingredients list
    def getIngL(self):
        return self.__ingL
    
    #Returns the object parts as a dict
    def toDict(self):
        output = {}
        for var in vars(self).keys():
            output[var.split("__")[-1]] = vars(self)[var]
        return output