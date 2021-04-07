#!/usr/bin/env python3
	


	
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
