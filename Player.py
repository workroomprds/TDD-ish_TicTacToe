#!/usr/bin/env python3

class Player():
	def __init__(self, name_list:list=["X","Y","Z"]):
		"""Takes two player names, or defaults to X and Y"""
		self.name_list = name_list
		self.index = 0
		
	def switch(self):
		"""Change current player"""
		self.index = (1+self.index) % len(self.name_list)
		
	def name(self):
		"""Return current player name"""
		return(self.name_list[self.index])

	
def test():
	"""To test code in this module"""
	pl = Player()
	assert(pl.name() == "X")
	pl.switch()
	assert(pl.name() == "Y")
	pl.switch()
	assert(pl.name() == "Z")
	pl.switch()
	assert(pl.name() == "X")
	
	pl2= Player(["X", "O"])
	assert(pl2.name() == "X")
	pl2.switch()
	assert(pl2.name() == "O")
	
	
test()

## For writing test-first python