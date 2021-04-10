#!/usr/bin/env python3

from Game import Game

class BoardAnalyser():
	"""Routines to decide winner, see avilable postions etc. Takes board as a parameter to fn, not as composition / inherited (this could change)"""
	def __init__(self, still_to_play_message="Still to play", draw_message="Draw", matching_size=3):
		self.still_to_play_message = still_to_play_message
		self.draw_message = draw_message
		self.matching_size = matching_size
		self.off_board = "off board"
		self.empty_space = " "
		
	def getItem(self, x:int, y:int, board)->str:
		"""Returns the content of a referenced cell on the board - and returns <self.off_board> if the cell is off the edge"""
		if (x<0) or (y<0):
			return(self.off_board)
		try:
			item = board[y][x]
		except:
			item = self.off_board
		return(item)
	
	def matching_set(self, list_to_check:list)->bool:
		"""Returns true if list is all the same"""
		return(len(set(list_to_check)) == 1)
	
	def list_of_items(self, board, start_x, start_y, inc_x, inc_y):
		"""Returns list of items from board, of size, starting at start_z, start_y, going in direction inc_x, inc_y"""
		outbound = []
		x = start_x
		y = start_y
		for i in range(self.matching_size):
			outbound.append(self.getItem(x, y, board))
			x += inc_x
			y += inc_y
		return outbound
	
	def horizontal_list(self, board, start_x, start_y):
		return(self.list_of_items(board, start_x, start_y, 1, 0))
	
	def vertical_list(self, board, start_x, start_y):
		return(self.list_of_items(board, start_x, start_y, 0, 1))
	
	def diag_list_tlbr(self, board, start_x, start_y):
		return(self.list_of_items(board, start_x, start_y, 1, 1))
	
	def diag_list_trbl(self, board, start_x, start_y):
		return(self.list_of_items(board, start_x, start_y, -1, 1))
	
	def cell_has_entry(self, item:str)->bool:
		"""Returns true if item neither <emptystring> nor <space>"""
		return(not(item==self.off_board or item==self.empty_space))
	
	def available_postitions(self, game:Game)->list:
		"""Returns all unplayed calls, referenced by board refs from Game"""
		available=[]
		for rowNumber, row in enumerate(game.board):
			for columnNumber, item in enumerate(row):
				if not(self.cell_has_entry(item)):
					available.append("".join([game.rowLabels[rowNumber],game.headerLabels[columnNumber]]))
		return available		
	
	def whoWins(self, board)->str:
		"""Checks a board for horizontal 3s, vertical 3s, TLBR 3s and TRBL 3s, returning the player mark for the first it finds. Returns messages if no winner - either <still to play>, or <draw> - messages as set in init"""
		still_to_play = False
		getItem = self.getItem
		for rowNumber, row in enumerate(board):
			for columnNumber, item in enumerate(row):
				if self.cell_has_entry(item):
					matching_row =     self.matching_set(self.horizontal_list(board, columnNumber, rowNumber))
					matching_col =     self.matching_set(self.vertical_list(board, columnNumber, rowNumber))
					matching_dia =     self.matching_set(self.diag_list_trbl(board, columnNumber, rowNumber))
					matching_opp_dia = self.matching_set(self.diag_list_tlbr(board, columnNumber, rowNumber))
					
					if (matching_row or matching_col or matching_dia or matching_opp_dia):
						return(item) ## whether still_to_play, or not.
				else:
					still_to_play = True
		return self.still_to_play_message if still_to_play else self.draw_message
	
	def keep_going(self, board)->bool:
		"""Returns True if nobody has won, and if there are still spaces left to play into"""
		return ( self.whoWins(board) == self.still_to_play_message )
	
	
def test():
	from TableMaker import TableMaker
	from Game import Game

	stillToPlay3x3 = [["X", " ", "X"],["O", " ", "X"],["X", "O", " "]] #No winner, still to play
	xWinsH3x3 = [["X", "X", "X"],["O", " ", "X"],["X", "O", " "]] #Horzontal
	xWinsV3x3 = [["X", "O", "X"],["X", " ", "X"],["X", "O", " "]] #Vertical
	xWinsD3x3 = [["X", "O", "X"],["O", "X", "O"],["X", "O", "X"]] #Diagonal
	xWinsOppositeD3x3 = [["O", "O", "X"],["O", "X", "O"],["X", "O", " "]] #Other Diagonal
	oWinsV3x3 = [["X", "O", "X"],["X", "O", "O"],["O", "O", "X"]] #O wins
	noWin3x3  = [["X", "O", "X"],["X", "O", "O"],["O", "X", "O"]] #no winner
	
	
	
	b=BoardAnalyser("go", "dr")
	game = Game(3, TableMaker)
	
	assert (b.getItem(-1, -1, xWinsH3x3) == b.off_board)
	assert (b.getItem(0, 0, xWinsH3x3) == "X")
	assert (b.getItem(0, 1, xWinsH3x3) == "O")
	assert (b.getItem(3, 3, xWinsH3x3) == b.off_board)
	assert (b.whoWins(xWinsD3x3) == "X")
	assert (b.whoWins(xWinsOppositeD3x3) == "X")
	assert (b.whoWins(xWinsH3x3) == "X")
	assert (b.whoWins(xWinsV3x3) == "X")
	assert (b.whoWins(xWinsD3x3) == "X")
	assert (b.whoWins(oWinsV3x3) == "O")
	assert (b.whoWins(noWin3x3) == "dr")
	assert (b.whoWins(stillToPlay3x3) == "go")
	assert (b.keep_going(stillToPlay3x3) == True)
	assert (b.keep_going(oWinsV3x3) == False)
	assert (b.keep_going(noWin3x3) == False)
	assert (b.cell_has_entry("A") == True)
	assert (b.cell_has_entry(b.empty_space) == False)
	assert (b.cell_has_entry(b.off_board) == False)
	
	xWinsH3x3 = [["X", "X", "X"],["O", " ", "X"],["X", "O", " "]] #Horzontal
	assert (b.list_of_items(xWinsH3x3, 0, 0, 1, 0) 	== ['X', 'X', 'X'])
	assert (b.horizontal_list(xWinsH3x3, 0, 0) 		== ['X', 'X', 'X'])
	assert (b.list_of_items(xWinsH3x3, 0, 1, 1, 0)  == ["O", " ", "X"])
	assert (b.horizontal_list(xWinsH3x3, 0, 1) 		== ["O", " ", "X"])
	assert (b.list_of_items(xWinsH3x3, 0, 0, 0, 1)  == ["X", "O", "X"])
	assert (b.vertical_list(xWinsH3x3, 0, 0) 		== ["X", "O", "X"])
	assert (b.list_of_items(xWinsH3x3, 0, 0, 1, 1) 	== ["X", " ", " "])
	assert (b.diag_list_tlbr(xWinsH3x3, 0, 0) 		== ["X", " ", " "])
	assert (b.list_of_items(xWinsH3x3, 2, 0, -1, 1) == ["X", " ", "X"])
	assert (b.diag_list_trbl(xWinsH3x3, 2, 0) 		== ["X", " ", "X"])
	
	game.update_whole_board([["X", "O", " "], ["X", "X", "O"], ["O", " ", "X"]])
	assert(b.available_postitions(game) == ["A3", "C2"])

test()
