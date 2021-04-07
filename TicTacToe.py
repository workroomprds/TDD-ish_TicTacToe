#!/usr/bin/env python3
	
from TableMaker import TableMaker

	
#--- end of test
#--- functions

class BoardAnalyser():
	"""Routines to decide winner, see avilable postions etc."""
	def __init__(self):
		pass
		
	def getItem(self, x, y, board):
		try:
			item = board[y][x]
		except:
			item = ""
		return(item)
	
	def matching_set(self, list_to_check):
		return(len(set(list_to_check)) == 1)
	
	def unplayed(self, item):
		return(item=="" or item==" ")
	
	def available_postitions(self, board, gameTable):
		available=[]
		for rowNumber, row in enumerate(board):
			for columnNumber, item in enumerate(row):
				if self.unplayed(item):
					available.append("".join([gameTable.rowLabels[rowNumber],gameTable.headerLabels[columnNumber]]))
		return available		
	
	def whoWins(self, board):
		still_to_play = False
		getItem = self.getItem
		for rowNumber, row in enumerate(board):
			for columnNumber, item in enumerate(row):
				if self.unplayed(item):
					still_to_play = True
				matching_row = self.matching_set([item, getItem(columnNumber+1, rowNumber, board), getItem(columnNumber+2, rowNumber, board)])
				matching_col = self.matching_set([item, getItem(columnNumber, rowNumber+1, board), getItem(columnNumber, rowNumber+2, board)])
				matching_dia = self.matching_set([item, getItem(columnNumber+1, rowNumber+1, board), getItem(columnNumber+2, rowNumber+2, board)])
				if (matching_row or matching_col or matching_dia):
					return(item) ## whether still_to_play, or not.
		return "Still to play" if still_to_play else "Draw"	
	


def announceWinner(winner):
	return(winner+" wins!" if (winner!="Draw") else "Draw")


def test_Analyser():
	stillToPlay3x3 = [["X", " ", "X"],["O", " ", "X"],["X", "O", " "]] #No winner, still to play
	xWinsH3x3 = [["X", "X", "X"],["O", " ", "X"],["X", "O", " "]] #Horzontal
	xWinsV3x3 = [["X", "O", "X"],["X", " ", "X"],["X", "O", " "]] #Vertical
	xWinsD3x3 = [["X", "O", "X"],["O", "X", "O"],["X", "O", "X"]] #Diagonal
	oWinsV3x3 = [["X", "O", "X"],["X", "O", "O"],["O", "O", "X"]] #O wins
	noWin3x3  = [["X", "O", "X"],["X", "O", "O"],["O", "X", "O"]] #no winner
	
	b=BoardAnalyser()
	
	assert (b.getItem(0, 0, xWinsH3x3) == "X")
	assert (b.getItem(0, 1, xWinsH3x3) == "O")
	assert (b.getItem(3, 3, xWinsH3x3) == "")
	assert (b.whoWins(xWinsH3x3) == "X")
	assert (b.whoWins(xWinsV3x3) == "X")
	assert (b.whoWins(xWinsD3x3) == "X")
	assert (b.whoWins(oWinsV3x3) == "O")
	assert (b.whoWins(noWin3x3) == "Draw")
	assert (b.whoWins(stillToPlay3x3) == "Still to play")
	
	game_surface = TableMaker(3)
	drawTable = game_surface.drawTable
	board = [["X", "O", " "], ["X", "X", "O"], ["O", " ", "X"]]
	assert(b.available_postitions(board, game_surface) == ["A3", "C2"])
	
def test_Winner():
	assert (announceWinner("Q") == "Q wins!")
	assert (announceWinner("Draw") == "Draw")
	

test_Analyser()
test_Winner()

## Examples
game_surface = TableMaker(3)
analyser = BoardAnalyser()
board = [["X", "O", " "], ["X", "X", "O"], ["O", " ", "X"]]
print(analyser.available_postitions(board, game_surface))
print(game_surface.drawTable(board))
print(announceWinner(analyser.whoWins(board)))


#print(drawTable(9))
#print(drawTable(3, [["X", "O", " "], ["X", "X", "O"], ["O", "O", "X"]]))
#print(drawTable(3))
