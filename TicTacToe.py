#!/usr/bin/env python3
	
from TableMaker import TableMaker
from BoardAnalyser import BoardAnalyser
from Game import Game
from Player import Player
import utils
import ui
	

game = Game(size=8, Surface=TableMaker)
analyser = BoardAnalyser(matching_size=3)
player = Player(["X", "O"])

while analyser.keep_going(game.board):
	ui.output(game.draw_table())
	player_move = ui.request_valid_input(player.name(), analyser.available_postitions(game), ui.askForInput)
	row = player_move[0] ## y axis
	col = player_move[1] ## x axis
	game.make_change(row, col, player.name())
	player.switch()

ui.output(game.draw_table())
ui.output("---------")
ui.output("That's it - game over!")
ui.output(ui.announceWinner(analyser.whoWins(game.board)))#
