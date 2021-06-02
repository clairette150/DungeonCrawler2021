from model.AbstractObject import AbstractObject
class Tile(AbstractObject):
	def __init__(self, x, y, tile_type):
		super().__init__(tile_type)
		self.x = x
		self.y = y
		self.tile_type = tile_type
