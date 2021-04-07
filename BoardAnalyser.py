#!/usr/bin/env python3

from Game import Game

class BoardAnalyser():
	"""Routines to decide winner, see avilable postions etc."""
	def __init__(self, still_to_play_message="Still to play", draw_message="Draw"):
		self.still_to_play_message = still_to_play_message
		self.draw_message = draw_message
		
	def getItem(self, x, y, board):
		try:
			item = board[y][x]
		except:
			item = ""
		return(item)
	
	def matching_set(self, list_to_check:list)->bool:
		return(len(set(list_to_check)) == 1)
	
	def unplayed(self, item:str)->bool:
		return(item=="" or item==" ")
	
	def available_postitions(self, game:Game)->list:
		available=[]
		for rowNumber, row in enumerate(game.board):
			for columnNumber, item in enumerate(row):
				if self.unplayed(item):
					available.append("".join([game.rowLabels[rowNumber],game.headerLabels[columnNumber]]))
		return available		
	
	def whoWins(self, board)->str:
		still_to_play = False
		getItem = self.getItem
		for rowNumber, row in enumerate(board):
			for columnNumber, item in enumerate(row):
				if self.unplayed(item):
					still_to_play = True
				matching_row = self.matching_set([item, getItem(columnNumber+1, rowNumber, board), getItem(columnNumber+2, rowNumber, board)])
				matching_col = self.matching_set([item, getItem(columnNumber, rowNumber+1, board), getItem(columnNumber, rowNumber+2, board)])
				matching_dia = self.matching_set([item, getItem(columnNumber+1, rowNumber+1, board), getItem(columnNumber+2, rowNumber+2, board)])
				if not self.unplayed(item) and (matching_row or matching_col or matching_dia):
					return(item) ## whether still_to_play, or not.
		return self.still_to_play_message if still_to_play else self.draw_message
	
	def keep_going(self, board)->bool:
		return ( self.whoWins(board) == self.still_to_play_message )
	
	
def test():
	from TableMaker import TableMaker
	from Game import Game

	stillToPlay3x3 = [["X", " ", "X"],["O", " ", "X"],["X", "O", " "]] #No winner, still to play
	xWinsH3x3 = [["X", "X", "X"],["O", " ", "X"],["X", "O", " "]] #Horzontal
	xWinsV3x3 = [["X", "O", "X"],["X", " ", "X"],["X", "O", " "]] #Vertical
	xWinsD3x3 = [["X", "O", "X"],["O", "X", "O"],["X", "O", "X"]] #Diagonal
	oWinsV3x3 = [["X", "O", "X"],["X", "O", "O"],["O", "O", "X"]] #O wins
	noWin3x3  = [["X", "O", "X"],["X", "O", "O"],["O", "X", "O"]] #no winner
	
	b=BoardAnalyser("go", "dr")
	game = Game(3, TableMaker)
	
	assert (b.getItem(0, 0, xWinsH3x3) == "X")
	assert (b.getItem(0, 1, xWinsH3x3) == "O")
	assert (b.getItem(3, 3, xWinsH3x3) == "")
	assert (b.whoWins(xWinsH3x3) == "X")
	assert (b.whoWins(xWinsV3x3) == "X")
	assert (b.whoWins(xWinsD3x3) == "X")
	assert (b.whoWins(oWinsV3x3) == "O")
	assert (b.whoWins(noWin3x3) == "dr")
	assert (b.whoWins(stillToPlay3x3) == "go")
	assert (b.keep_going(stillToPlay3x3) == True)
	assert (b.keep_going(oWinsV3x3) == False)
	assert (b.keep_going(noWin3x3) == False)
	
	game.update_whole_board([["X", "O", " "], ["X", "X", "O"], ["O", " ", "X"]])
	assert(b.available_postitions(game) == ["A3", "C2"])

test()
