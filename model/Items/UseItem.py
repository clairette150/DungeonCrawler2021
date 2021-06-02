from model.Items.Item import Item

class UseItem(Item):
    def __init__(self, id=0, name="nothing", desc="", useable=False, equipable=False, quality=0, icon = "i",  ingL=[] ,use=lambda x: None):
        super().__init__(id, name, desc, useable, equipable, quality, icon, ingL)
        self.use = use
