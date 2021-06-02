import os

from read_write_csv import make_csv, read_csv, add_csv


class TileType:
	def __init__(self, name, walkability, icon):
		self.name = name
		self.walkability = walkability
		self.icon = icon
		
	def __repr__(self):
		return self.icon
		


class TileTypeFactory:
	path = './.temp/tile_types.csv'
	def __init__(self):
		pass
			
	def read_tiles_from_csv(self):
		try:
			data = read_csv(self.path)
			#print("Got the following tiletype data: ", data)
			return data
		except FileNotFoundError:
			return False
		
	def make_tile_obj_dict(self, data):
		dictionary_of_tile_types = {}
		# add each type to dictionary:
		for tileData in data:
			try:
				name, walkability, icon =tileData
				dictionary_of_tile_types[name] = TileType(name, walkability, icon)
			except:
				pass
		return dictionary_of_tile_types
		
	def create_tile_types(self):
		if not os.path.isfile(self.path):
			# create file
			make_csv(self.path,['name', 'walkability', 'icon'])
			# fill it with some tile type data
			basic_tile_type_list = [["ground", True, "•"],["wall", False, "#"],["water", False, "~"],["altar", False, "@"],["grass", True, "*"], ["unknown", True, "?"]]
			for data in basic_tile_type_list:
				add_csv(self.path, data)
			
	def make_dictionary(self):
		data = self.read_tiles_from_csv()
		if data == False:
			self.create_tile_types()
			data = self.read_tiles_from_csv()
		return self.make_tile_obj_dict(data) 
		
	
tile_type_factory = TileTypeFactory()	
tile_types = tile_type_factory.make_dictionary()


#if __name__ == "__main__":
	#Testing
	#tile_type_factory = TileTypeFactory()
	#data = tile_type_factory.read_tiles_from_csv()
	#if data == False:
	#	tile_type_factory.create_tile_types()
	#	data = tile_type_factory.read_tiles_from_csv()
	#print("Got the following tiletype data: ", type(data), ",", data)
