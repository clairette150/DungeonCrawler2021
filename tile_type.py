from json import JSONEncoder


class TileTypeEncoder(JSONEncoder):
    def default(self, object):
        if isinstance(object, TileType):
            return object.__dict__
        else:
            # raising exceptions for unsupported types
            return json.JSONEncoder.default(self, object)


class TileType:
	def __init__(self, name, walkability, icon):
		super().__init__
		self.name = name
		self.walkability = walkability
		self.icon = icon
	
	def __repr__(self):
		return self.icon

ground = TileType("ground", True, "•")
wall = TileType("wall", False, "#")
water = TileType("water", False, "~")
altar = TileType("altar", False, "@")
grass = TileType("grass", True, "*")
unknown = TileType("unknown", True, "?")




#json_string = TileTypeEncoder().encode(ground)
#print(json_string)
