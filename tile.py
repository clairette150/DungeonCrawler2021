from json import JSONEncoder

from tile_type import ground, wall

class Tile():
	def __init__(self, x, y, tile_type):
		self.x = x
		self.y = y
		self.tile_type = tile_type


class TileEncoder(JSONEncoder):
    def default(self, object):
        if isinstance(object, Tile):
            return object.__dict__
        else:
            # raising exceptions for unsupported types
            return json.JSONEncoder.default(self, object)

