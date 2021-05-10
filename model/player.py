from model.point import Point

class Player:
	#Constructor
	def __init__(self):
		self.name = "Jane"
		self.hp = 10
		self.mp = 0
		self.x = 1
		self.y = 1
		self.pos = Point(self.x, self.y)
		self.icon = "o"


    # Prints the current player stats to console.
	def printStats(self):
		print("Player: {name} | HP: {hp} | MP: {mp}".format(name=self.name, hp=self.hp, mp=self.mp))

	def move(self):
		#TODO: Implement
		pass