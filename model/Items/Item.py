class Item:
    #TODO: add sprite /icon field.

    # Creates an item where:
    # id(default:0) is the item id
    # name(default:"") is the name of the item.
    # desc(default:"") is the description of the item.
    # useable(default: False) is the item useable?
    # equipable(default:False) is the item equipable?
    # quality(default:0) is the quality of the item.
    def __init__(self, id=0, name="", desc="", useable=False, equipable=False, quality=0):
        self.__id = id
        self.__name = name
        self.__desc = desc
        self.__useable = useable
        self.__equipable = equipable
        self.__quality = quality

    # Returns item id.
    def getItemId(self):
        return self.__id

    # Returns item name.
    def getName(self):
        return self.__name

    # Returns item description.
    def getDescription(self):
        return self.__desc

    # Returns if the item is equipable.
    def isEquipable(self):
        return self.__equipable

    # Returns if the item is useable.
    def isUseable(self):
        return self.__useable

    # Returns if the item quality.
    def getQuality(self):
        return self.__quality