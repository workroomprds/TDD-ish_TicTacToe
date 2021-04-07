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

def matching_set(list_to_check):
	return(len(set(list_to_check)) == 1)

def unplayed(item):
	return(item=="" or item==" ")

def available_postitions(board, gameTable):
	available=[]
	for rowNumber, row in enumerate(board):
		for columnNumber, item in enumerate(row):
			if unplayed(item):
				available.append("".join([gameTable.rowLabels[rowNumber],gameTable.headerLabels[columnNumber]]))
	return available		

def whoWins(board):
	still_to_play = False
	for rowNumber, row in enumerate(board):
		for columnNumber, item in enumerate(row):
			if unplayed(item):
				still_to_play = True
			matching_row = matching_set([item, getItem(columnNumber+1, rowNumber, board), getItem(columnNumber+2, rowNumber, board)])
			matching_col = matching_set([item, getItem(columnNumber, rowNumber+1, board), getItem(columnNumber, rowNumber+2, board)])
			matching_dia = matching_set([item, getItem(columnNumber+1, rowNumber+1, board), getItem(columnNumber+2, rowNumber+2, board)])
			if (matching_row or matching_col or matching_dia):
				return(item) ## whether still_to_play, or not.
	return "Still to play" if still_to_play else "Draw"	

def announceWinner(winner):
	return(winner+" wins!" if (winner!="Draw") else "Draw")


def test_Winner():
	stillToPlay3x3 = [["X", " ", "X"],["O", " ", "X"],["X", "O", " "]] #No winner, still to play
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
	assert (whoWins(noWin3x3) == "Draw")
	assert (whoWins(stillToPlay3x3) == "Still to play")
	assert (announceWinner("Q") == "Q wins!")
	assert (announceWinner("Draw") == "Draw")
	
	game_surface = TableMaker(3)
	drawTable = game_surface.drawTable
	board = [["X", "O", " "], ["X", "X", "O"], ["O", " ", "X"]]
	assert(available_postitions(board, game_surface) == ["A3", "C2"])
	


test_Winner()

## Examples
game_surface = TableMaker(3)
drawTable = game_surface.drawTable
board = [["X", "O", " "], ["X", "X", "O"], ["O", " ", "X"]]
print(available_postitions(board, game_surface))
print(drawTable(board))
#print(announceWinner(whoWins(board)))


#print(drawTable(9))
#print(drawTable(3, [["X", "O", " "], ["X", "X", "O"], ["O", "O", "X"]]))
#print(drawTable(3))
