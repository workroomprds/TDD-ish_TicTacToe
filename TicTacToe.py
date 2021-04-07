#!/usr/bin/env python3
	
from TableMaker import TableMaker
from BoardAnalyser import BoardAnalyser
from Board import Board
import utils
import ui
	
	

def switchPlayer(player):
	return( "X" if player == "Y" else "Y")

board = Board(3)
game_surface = TableMaker(3)
analyser = BoardAnalyser()
player = "X"
while analyser.whoWins(board.board) == "Still to play":
	ui.output(game_surface.drawTable(board.board))
	move = ui.request_valid_input(player, analyser.available_postitions(board.board, game_surface), ui.askForInput)
	row = move[0] ## y axis
	col = move[1] ## x axis
	board.make_change(row, col, player, game_surface)
	player = switchPlayer(player)

ui.output(game_surface.drawTable(board.board))
ui.output("---------")
ui.output("That's it - game over!")
ui.output(announceWinner(analyser.whoWins(board.board)))#

