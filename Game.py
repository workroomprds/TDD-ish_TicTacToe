#!/usr/bin/env python3

class Game():
	def __init__(self, size, Surface):
		self.board = self.empty_board(size)
		self.surface = Surface(size)
		self.rowLabels = self.surface.rowLabels
		self.headerLabels = self.surface.headerLabels
		
	def draw_table(self):
		return self.surface.drawTable(self.board)
		
	def empty_board(self,size):
		board = []
		for i in range(0,size):
			row = []
			for j in range(0,size):
				row.append(" ")
			board.append(row)
		return(board)
	
	def make_change(self, x, y, content):
		"""Makes a change to the board, based on labels given - no validation of input, not of board capacity, nor of content"""
		self.board[self.rowLabels.index(x)][self.headerLabels.index(y)] = content
		
	def update_whole_board(self, new_board):
		self.board = new_board
	
	
def test():
	from TableMaker import TableMaker
	
	this_game = Game(3, TableMaker)
	
	boardWithXinB1 = """    1   2   3
   --- --- ---
A |   |   |   |
   --- --- ---
B | X |   |   |
   --- --- ---
C |   |   |   |
   --- --- ---"""
	
	assert(this_game.board == [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]])
	
	this_game.make_change("B", "1", "X")
	assert(this_game.draw_table() == boardWithXinB1)
	
	this_game.update_whole_board([["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]])
	assert(this_game.board == [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]])
	
test()

