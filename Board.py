#!/usr/bin/env python3

from TableMaker import TableMaker
from BoardAnalyser import BoardAnalyser

class Board():
	def __init__(self,size,Surface):
		self.board = self.empty_board(size)
		
	def empty_board(self,size):
		board = []
		for i in range(0,size):
			row = []
			for j in range(0,size):
				row.append(" ")
			board.append(row)
		return(board)
	
	def make_change(self, x, y, content, surface):
		"""Makes a change to the board, based on labels given - no validation of input, not of board capacity, nor of content"""
		self.board[surface.rowLabels.index(x)][surface.headerLabels.index(y)] = content
		
	def update_whole_board(self, new_board):
		self.board = new_board
	
	
def test_Board():
	this_game = Board(3)
	show_table = TableMaker(3)
	analyst = BoardAnalyser()
	
	boardWithXin11 = """    1   2   3
   --- --- ---
A | X |   |   |
   --- --- ---
B |   |   |   |
   --- --- ---
C |   |   |   |
   --- --- ---"""
	
	assert(this_game.board == [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]])
	
	this_game.make_change("A", "1", "X", show_table)
	assert(show_table.drawTable(this_game.board) == boardWithXin11)
	this_game.make_change("B", "2", "X", show_table)
	this_game.make_change("C", "3", "X", show_table)
	assert(analyst.available_postitions(this_game.board, show_table) == ['A2', 'A3', 'B1', 'B3', 'C1', 'C2'])
	assert(analyst.whoWins(this_game.board) == "X")
	
	
test_Board()


## For writing test-first python