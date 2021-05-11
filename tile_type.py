class TileType():
	def __init__(self, name, walkability, icon):
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
