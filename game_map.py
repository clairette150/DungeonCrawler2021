# Game Map

import os 

from tile import Tile
from tile_type import ground, wall

from read_write_csv import make_csv, read_csv, add_csv


class GameMap():
	def __init__(self):
		self.board = []		
		self.width = 0
		self.heigth = 0
		self.tile_types = {"wall":wall, "ground":ground} # import from tile_types and add more here 
		
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
	
	def create_new_tile(self, tile_x, tile_y, tile_name):
		tile_obj = Tile(tile_x, tile_y, self.tile_types[tile_name])
		dictionary = {'x':tile_x, 'y':tile_y, 'tile':tile_obj}
		self.board.append(dictionary)
			
	def write_game_map(self, tiles_of_map_data):
		# add to csv file
		for tile in tiles_of_map_data:
			add_csv('tile_map.csv',tile)
		
	def create_game_map(self):
		if not os.path.isfile('./tile_map.csv'): 
			make_csv('tile_map.csv',['x','y','tiletype'])
		
	def set_size(self, new_width, new_heigth):
		self.width = new_width
		self.heigth = new_heigth
	

if __name__ == "__main__":
	game_map = GameMap()
	#game_map.create_game_map()
	#data = game_map.read_map()
	#game_map.write_map([['0','0','wall'], ['0','1','wall'], ['0','2','wall'], ['1','0','ground'], ['1','1','ground'], ['1','2','ground'], ['2','0','wall'], ['2','1','wall'], ['2','2','wall']])
	#data = game_map.read_map()
	#game_map.make_board()	
	#game_map.draw_map()
		
