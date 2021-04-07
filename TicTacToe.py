#!/usr/bin/env python3
	
from TableMaker import TableMaker
from BoardAnalyser import BoardAnalyser

	
#--- end of test
#--- functions


	
	
def announceWinner(winner):
	return(winner+" wins!" if (winner!="Draw") else "Draw")


def test_Winner():
	assert (announceWinner("Q") == "Q wins!")
	assert (announceWinner("Draw") == "Draw")
	

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
