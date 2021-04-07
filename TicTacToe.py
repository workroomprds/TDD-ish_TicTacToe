#!/usr/bin/env python3
	
from TableMaker import TableMaker

	
#--- end of test
#--- functions


def getItem(x,y,board):
	try:
		item = board[y][x]
	except:
		item = ""
	return(item)

def whoWins(board):
	for rowNumber, row in enumerate(board):
		for columnNumber, item in enumerate(row):
			if ((item == getItem(columnNumber+1, rowNumber, board)) and (item == getItem(columnNumber+2, rowNumber, board)) and (item != "")):
				return(item)
			if ((item == getItem(columnNumber, rowNumber+1, board)) and (item == getItem(columnNumber, rowNumber+2, board)) and (item != "")):
				return(item)
			if ((item == getItem(columnNumber+1, rowNumber+1, board)) and (item == getItem(columnNumber+2, rowNumber+2, board)) and (item != "")):
				return(item)
	return("")
#what about an unfinished board?

def announceWinner(winner):
	return(winner+" wins!" if (winner!="") else "Draw")


def test_Winner():
	xWinsH3x3 = [["X", "X", "X"],["O", " ", "X"],["X", "O", " "]] #Horzontal
	xWinsV3x3 = [["X", "O", "X"],["X", " ", "X"],["X", "O", " "]] #Vertical
	xWinsD3x3 = [["X", "O", "X"],["O", "X", "O"],["X", "O", "X"]] #Diagonal
	oWinsV3x3 = [["X", "O", "X"],["X", "O", "O"],["O", "O", "X"]] #O wins
	noWin3x3  = [["X", "O", "X"],["X", "O", "O"],["O", "X", "O"]] #no winner
	
	assert (getItem(0, 0, xWinsH3x3) == "X")
	assert (getItem(0, 1, xWinsH3x3) == "O")
	assert (getItem(3, 3, xWinsH3x3) == "")
	assert (whoWins(xWinsH3x3) == "X")
	assert (whoWins(xWinsV3x3) == "X")
	assert (whoWins(xWinsD3x3) == "X")
	assert (whoWins(oWinsV3x3) == "O")
	assert (whoWins(noWin3x3) == "")
	assert (announceWinner("Q") == "Q wins!")
	assert (announceWinner("") == "Draw")
	


test_Winner()

## Examples
game_surface = TableMaker(3)
drawTable = game_surface.drawTable
#print(drawTable(9))
#print(drawTable(3, [["X", "O", " "], ["X", "X", "O"], ["O", "O", "X"]]))
#print(drawTable(3))
board = [["X", "O", " "], ["X", "X", "O"], ["O", "O", "X"]]
print(drawTable(board))
print(announceWinner(whoWins(board)))
