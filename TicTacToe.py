#!/usr/bin/env python3
	
from TableMaker import TableMaker
from BoardAnalyser import BoardAnalyser
from Game import Game
import utils
import ui
	
class Player():
	def __init__(self, first_player:str="X", second_player:str="Y"):
		self.first_player = first_player
		self.second_player = second_player
		self.player_name = first_player
	
	def switch(self):
		self.player_name = self.second_player if (self.player_name == self.first_player) else self.first_player
		
	def name(self):
		return(self.player_name)
	
	
game = Game(3, TableMaker)
analyser = BoardAnalyser()
player = Player("X", "O")

while analyser.keep_going(game.board):
	ui.output(game.draw_table())
	move = ui.request_valid_input(player.name(), analyser.available_postitions(game), ui.askForInput)
	row = move[0] ## y axis
	col = move[1] ## x axis
	game.make_change(row, col, player.name())
	player.switch()

ui.output(game.draw_table())
ui.output("---------")
ui.output("That's it - game over!")
ui.output(ui.announceWinner(analyser.whoWins(game.board)))#
