# Game Map

import os 

from tile import Tile
from tile_type import ground, wall, water, altar, grass

from read_write_csv import make_csv, read_csv, add_csv


class GameMap():
	def __init__(self):
		self.board = []		
		self.width = 0
		self.heigth = 0
		self.tile_types = {"wall":wall, "ground":ground, "water":water, "altar":altar,"grass":grass} # import from tile_types and add more here
		
	def read_map(self):
		# read from csv file
		data = read_csv('tile_map.csv')
		return data
	
	def make_board(self):
		# make game board from read in csv data:
		max_x = 0
		max_y = 0
		data = self.read_map()	
		print(data[1:len(data)])
		for tile_data in data[1:len(data)]:
			print(tile_data)
			try:
				tile_x, tile_y, tile_name = tile_data
				tile_x = int(tile_x)
				tile_y = int(tile_y)
				tile_obj = Tile(tile_x, tile_y, self.tile_types[tile_name])
				dictionary = {'x':tile_x, 'y':tile_y, 'tile':tile_obj}
				if tile_x > max_x:
					max_x = tile_x
				if tile_y > max_y:
					max_y = tile_y
				print("adding {} to game board at ({}/{})". format(tile_name, tile_x, tile_y))
				self.board.append(dictionary)
				self.width = int(max_y)
				self.heigth = int(max_x)
			except:
				# Do nothing here
				pass
	
	def create_new_tile(self, tile_x, tile_y, tile_name):
		tile_obj = Tile(tile_x, tile_y, self.tile_types[tile_name])
		dictionary = {'x':tile_x, 'y':tile_y, 'tile':tile_obj}
		self.board.append(dictionary)
			
	def write_game_map(self, data):
		# add to csv file
		for tile_dict in self.board:
			print(tile_dict)
			data_list = []
			data_list.append(tile_dict['x'])
			data_list.append(tile_dict['y'])
			data_list.append(tile_dict['tile'].tile_type.name)
			print("-- writing tiledata to csv: ", data_list)
			add_csv('tile_map.csv',data_list)
		
	def create_game_map(self):
		if not os.path.isfile('./tile_map.csv'): 
			# create a csv
			make_csv('tile_map.csv',['x','y','tiletype'])
			# fill it with tiles
			self.game_map.write_game_map([['0','0','wall'], ['0','1','wall'], ['0','2','wall'], ['1','0','ground'], ['1','1','ground'], ['1','2','ground'], ['2','0','wall'], ['2','1','wall'], ['2','2','wall']])
			
			
	def save_game_map(self):
		# this over-writes the tilemap
		data_list = [['x','y','tiletype']]
		for tile_dict in self.board:
			print(tile_dict)
			data_list = []
			data_list.append(tile_dict['x'])
			data_list.append(tile_dict['y'])
			data_list.append(tile_dict['tile'].tile_type.name)
		print("-- writing tiledata to csv: ", data_list)
		add_csv('tile_map.csv', data_list)
		
	def write_game_map(self, tiles_of_map_data):
		# overwrite old file
		make_csv('tile_map.csv',['x','y','tiletype'])
		# add to csv file
		for tile in tiles_of_map_data:
			add_csv('tile_map.csv',tile)
		
	def set_size(self, new_width, new_heigth):
		self.width = new_width
		self.heigth = new_heigth
		
	def is_walkable(self, x, y):
		for tile in self.board:
			if x == tile['x'] and y == tile['y']:
				return tile['tile'].tile_type.walkability
	

if __name__ == "__main__":
	game_map = GameMap()
	#game_map.create_game_map()
	#data = game_map.read_map()
	
	#TODO: change this to dictionaries!
	#game_map.write_map([['0','0','wall'], ['0','1','wall'], ['0','2','wall'], ['1','0','ground'], ['1','1','ground'], ['1','2','ground'], ['2','0','wall'], ['2','1','wall'], ['2','2','wall']])
	
	#data = game_map.read_map()
	#game_map.make_board()	
	#game_map.draw_map()
		
