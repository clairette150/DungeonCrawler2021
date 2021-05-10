# Dungeon Crawler 2021
# by marionline

from os import system, name 
from time import sleep 
from model.player import Player
from model.point import Point

from game_map import GameMap

        
LEFT = Point(0, 1)
RIGHT = Point(0, -1)
UP = Point(-1, 0)
DOWN = Point(1,0)

class Display():
    def __init__(self):
        pass

    def printPlayerStat(self, player):
        print()
            
    def draw_map(self, game_map, player):
        y = 0
        x = 0
        while y <= game_map.width: 
            row = ""
            while x <= game_map.heigth:
                for tile_data in game_map.board:
                    #draw player
                    if x == player.x and y == player.y:
                        #print(x, "/", y)
                        icon = player.icon
                    #TODO add other icons like mobs, coins etc.
                    # draw map
                    elif x == tile_data['x'] and y == tile_data['y']:
                        icon = str(tile_data['tile'].tile_type)
                        break
                    else:
                        icon = "?"
                row += icon     
                x += 1
            x = 0
            y += 1
            print(row)
            
    def clear_screen(self): 
        # https://www.codespeedy.com/clear-screen-in-python/
        # for windows os
        if name == 'nt': 
            _ = system('cls')  
        # for mac and linux os(The name is posix)
        else: 
            _ = system('clear') 


class Game():
	def __init__(self):
		self.is_running = True
		self.game_map = GameMap()
		self.player = Player()
		self.display = Display()
		self.obj_on_screen = [] # maybe this goes into display?
		
	def run(self):
		self.set_up_map()
		while self.is_running:
			
			#show position
			print("Position: {}/{}".format(self.player.x, self.player.y))
			
			# handle input
			player_input = input("You:")
			
			# compute
			sleep(0.5)
			if player_input == "w":
				self.player.y += -1
			if player_input == "a":
				self.player.x += -1
			if player_input == "s":
				self.player.y += 1
			if player_input == "d":
				self.player.x += 1
				
			# Building Mode
			# - First alter map size
			# - Then add new tiles
			if player_input == "m":
				new_width = input("New Map Width: ")
				new_heigth = input("New Map Height: ")
				new_width = int(new_width)
				new_heigth = int(new_heigth) 
				self.game_map.set_size(new_width, new_heigth)
				# fill map with unkown tiles
				
			
			if player_input == "#":
				# create wall tile
				self.game_map.create_new_tile(self.player.x, self.player.y, "wall")
			if player_input == ".":
				# create ground tile
				self.game_map.create_new_tile(self.player.x, self.player.y, "ground")
			if player_input == "~":
				# create water tile
				self.game_map.create_new_tile(self.player.x, self.player.y, "water")
			if player_input == "@":
				# create altar tile
				self.game_map.create_new_tile(self.player.x, self.player.y, "altar")
			if player_input == "*":
				# create grass tile
				self.game_map.create_new_tile(self.player.x, self.player.y, "grass")

			#clear screen
			self.display.clear_screen()
			# show
			self.display.draw_map(self.game_map, self.player)
			# print player stats
			self.player.printStats()
					
	def quit(self):
		self.is_running = False
	
	def set_up_map(self):
			self.game_map.create_game_map()
			self.game_map.write_game_map([['0','0','wall'], ['0','1','wall'], ['0','2','wall'], ['1','0','ground'], ['1','1','ground'], ['1','2','ground'], ['2','0','wall'], ['2','1','wall'], ['2','2','wall']])
			self.game_map.make_board()	


if __name__      == "__main__":
    game = Game()
    game.run()
        
