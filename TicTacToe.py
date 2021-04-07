#!/usr/bin/env python3
	
from TableMaker import TableMaker
from BoardAnalyser import BoardAnalyser
from Game import Board
import utils
import ui
	
	

def switchPlayer(player):
	return( "X" if player == "Y" else "Y")

game = Board(3, TableMaker)
analyser = BoardAnalyser()
player = "X"

while analyser.keep_going(game.board):
	ui.output(game.draw_table())
	move = ui.request_valid_input(player, analyser.available_postitions(game), ui.askForInput)
	row = move[0] ## y axis
	col = move[1] ## x axis
	game.make_change(row, col, player)
	player = switchPlayer(player)

ui.output(game.draw_table())
ui.output("---------")
ui.output("That's it - game over!")
ui.output(ui.announceWinner(analyser.whoWins(game.board)))#
