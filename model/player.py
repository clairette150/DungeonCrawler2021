from model.point import Point
from model.AbstractObject import AbstractObject

class Player(AbstractObject):
	#Constructor
	def __init__(self):
		super(name)
		self.hp = 10
		self.mp = 0
		self.x = 1
		self.y = 1
		self.pos = Point(self.x, self.y)
		self.icon = "o"


    # Prints the current player stats to console.
	def printStats(self):
		print("Player: {name} | HP: {hp} | MP: {mp}".format(name=self.__name, hp=self.hp, mp=self.mp))

	# Changes the name of the player,
	# returns true when name got changed.
	def setName(self, name=""):
		if name == "":
			return False
		self.__name = name
		return True

	def move(self):
		#TODO: Implement
		pass
