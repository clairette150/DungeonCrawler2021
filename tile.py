from tile_type import ground, wall

class Tile():
	def __init__(self, x, y, tile_type):
		self.x = x
		self.y = y
		self.tile_type = tile_type
