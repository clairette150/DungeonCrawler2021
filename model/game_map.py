# Game Map

import os
from tile import Tile
from tile_type import tile_types
from model.Items.ItemRepository import ItemRepository
from read_write_csv import make_csv, read_csv, add_csv


class GameMap:
    def __init__(self):
        self.board =  {}
        self.width = 0
        self.heigth = 0
        self.tile_types = tile_types
        self.itemRepo = ItemRepository()
        #{"wall":wall, "ground":ground, "water":water, "altar":altar,"grass":grass, "unknown":unknown} # import from tile_types and add more here

    # Returns a list with items/tiles on position x,y
    # @params x - x coordinate
    # @params y - y coordinate
    def getTileAt(self, x, y):
        try:
            return self.board[x][y]
        except:
            return []
    #Checks if the directory is initalized on position x,y
    #otherwise it will create an empty list in it
    # @params x - x coordinate
    # @params y - y coordinate
    def checkForInitCell(self,x,y):
        try:
            test = self.board[x][y]
        except:
            try:
                test = self.board[x]
            except:
                self.board[x]= {}
            self.board[x][y] = []
    def read_map(self):
        # read from csv file
        data = read_csv('tile_map.csv')
        return data
    
    def make_board(self):
        # make game board from read in csv data:
        max_x = 0
        max_y = 0
        data = self.read_map()
        for tile_data in data[1:len(data)]:
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
                self.checkForInitCell(tile_x, tile_y)
                self.board[tile_x][tile_y].append(tile_obj)
                # maybe save game map?
                self.save_game_map()
            except:
                if(len(tile_data) > 0):
                    x = int(tile_data[0])
                    y = int(tile_data[1])
                    self.checkForInitCell(x, y)
                    #TODO: probably critical, use create_new_tile funciton nistead?
                    self.board[x][y].append(self.itemRepo.loadCustomItem(tile_data[2]))
                    if x > max_x:
                        max_x = x
                    if y > max_y:
                        max_y = y
            self.width = int(max_y)
            self.heigth = int(max_x)

    def create_new_tile(self, tile_x, tile_y, tile_name):
        if(None == tile_name):
            return
        if type(tile_name) == type("string"):
            tile_obj = Tile(tile_x, tile_y, self.tile_types[tile_name])
        else:
            tile_obj = tile_name
        self.checkForInitCell(tile_x, tile_y)
        self.board[tile_x][tile_y].append(tile_obj)

    #def write_game_map(self, data):
    #    # add to csv file
    #    for tile_dict in self.board:
    #        print(tile_dict)
    #        data_list = []
    #        data_list.append(tile_dict['x'])
    #        data_list.append(tile_dict['y'])
    #        data_list.append(tile_dict['tile'].tile_type.name)
    #        print("-- writing tiledata to csv: ", data_list)
    #        add_csv('tile_map.csv',data_list)

    def create_game_map(self):
        if not os.path.isfile('./tile_map.csv'):
            # create a csv
            make_csv('tile_map.csv',['x','y','tiletype'])
            # fill it with tiles
            self.write_game_map_first_time([['0','0','wall'], ['0','1','wall'], ['0','2','wall'], ['1','0','ground'], ['1','1','ground'], ['1','2','ground'], ['2','0','wall'], ['2','1','wall'], ['2','2','wall']])

    def save_game_map(self):
        # overwrite old file if existant
        make_csv('tile_map.csv',['x','y','tiletype'])
        data_list = []
        for x in self.board.keys():
            xList = self.board[x]
            for y in xList.keys():
                for entry in self.board[x][y]:
                    next_data = []
                    next_data.append(x)
                    next_data.append(y)
                    try:
                        next_data.append(entry.tile_type.name)
                    except:
                        next_data.append(entry.toDict())
                    data_list.append(next_data)
        #print("-- writing tiledata to csv: ", data_list)
        for element in data_list:
            add_csv('tile_map.csv', element)

    def write_game_map_first_time(self, tiles_of_map_data):
        # overwrite old file if existant
        make_csv('tile_map.csv',['x','y','tiletype'])
        # add to csv file
        for tile in tiles_of_map_data:
            add_csv('tile_map.csv',tile)

    def set_size(self, new_width, new_heigth):
        self.width = new_width
        self.heigth = new_heigth

    def is_walkable(self, x, y):
        try:
            return self.board[x][y][0].tile.tile_type.walkability
        except:
            return False
