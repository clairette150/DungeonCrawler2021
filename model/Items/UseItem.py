from model.Items.Item import Item
from copy import copy

class UseItem(Item):
    # TODO: Extend
    def __init__(self, id=0, name="nothing", desc="", useable=False, equipable=False, quality=0, use=lambda x: None):
        super().__init__(id, name, desc, useable, equipable, quality)
        self.use = use


