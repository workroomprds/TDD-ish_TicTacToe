#!/usr/bin/env python3
defaultTableHeaders = ["1", "2", "3", "4", "5", "6", "7", "8", "9"] #single chars onle
defaultRowLabels = ["A", "B", "C", "D", "E", "F", "G", "H", "I"] #single chars only

def test():
	
	# test routines to draw header, divider, empty and filled row, building tabls as a list, joining list with newline
	assert( makeHeaderRow(2, ["1", "2"]) == "    1   2"), "produced "+ makeHeaderRow(2, ["1", "2"]) 
	assert( drawEmptyRow("A",3) ==  "A |   |   |   |"), "produced "+drawRow("A",3) 
	assert( drawDivider(3) == "   --- --- ---")
	assert (drawFilledRow("A", 2, ["X", "O"]) =="A | X | O |")
	assert ( buildRowsIntoList("Labels", "Divider", ["Row1", "Row2"]) == ["Labels", "Divider", "Row1", "Divider", "Row2", "Divider"])
	assert( joinRowsWithNewLine(["A", "b"]) == """A
b""")
	
	
	
	# test table production - basic, 2x2, 3x3 filled, specialised labels
	# all table tests that expect default headers need to aling with defaults
	table11 = """    1
   ---
A |   |
   ---"""
	table22 = """    1   2
   --- ---
A |   |   |
   --- ---
B |   |   |
   --- ---"""

	dataForFilledTable33 = [["X", "O", " "], ["X", "X", "O"], ["O", "O", "X"]]
	filledTable33 = """    1   2   3
   --- --- ---
A | X | O |   |
   --- --- ---
B | X | X | O |
   --- --- ---
C | O | O | X |
   --- --- ---"""
	
	testTableMaker = TableMaker()
	drawTable = testTableMaker.drawTable
	
	assert( drawTable(1) == table11), "drawTable(1) produced "+drawTable(1)
	assert( drawTable(2) == table22), "drawTable(2) produced "+drawTable(2)
	assert ( drawTable(3, dataForFilledTable33) == filledTable33) # done as 'approval test'
	
	specialisedLabels = {"rowLabels":["X", "Y"], "headerLabels":["!","?"]}
	emptyTableDiffHeaders22 = """    !   ?
   --- ---
X |   |   |
   --- ---
Y |   |   |
   --- ---"""
	testTableMaker = TableMaker(specialisedLabels)
	assert ( testTableMaker.drawTable(2) == emptyTableDiffHeaders22) # done as 'approval test'

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
	
	
	
#--- end of test
#--- functions
def drawEmptyRow(rowInfo, size):
	return(rowInfo+" "+"|   "*size+"|")

def drawFilledRow(rowInfo, size, content):
	collection = [rowInfo+" "+"|"]
	for i in range(size):
		collection.append(" "+content[i]+" |")
	return("".join(collection))

def drawDivider(size):
	return("  "+" ---"*size)

def makeHeaderRow(numberOfColumns, contents):
	return("    "+"   ".join(contents[0:numberOfColumns]))

def joinRowsWithNewLine(target):
	return("\n".join(target))

def buildRowsIntoList(headerLabels, divider, rows):
	collection = []
	collection.append( headerLabels )
	collection.append( divider )
	for row in rows:
		collection.append( row )
		collection.append( divider )
	return(collection)

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

class TableMaker():
	
	def __init__(self,  parm = { "headerLabels":defaultTableHeaders, "rowLabels": defaultRowLabels}):
		self.rowLabels =    parm["rowLabels"]
		self.headerLabels = parm["headerLabels"]

	def drawTable(self, size, content=[]):		
		if (content !=[]):
			def drawRow(rowNumber):
				return(drawFilledRow(self.rowLabels[rowNumber], size, content[rowNumber]))
		else:
			def drawRow(rowNumber):
				return( drawEmptyRow(self.rowLabels[rowNumber], size) )
						
		myDivider = drawDivider(size) # one of these
		myColumnLabels = makeHeaderRow(size, self.headerLabels) # one of these
		rows = list(map(drawRow, range(size))) ## a list with as many rows as needed
		
		return(joinRowsWithNewLine(buildRowsIntoList(myColumnLabels, myDivider, rows)))
	
test() 
test_Winner()

## Examples
myTableMaker = TableMaker()
drawTable = myTableMaker.drawTable
#print(drawTable(9))
#print(drawTable(3, [["X", "O", " "], ["X", "X", "O"], ["O", "O", "X"]]))
#print(drawTable(3))
board = [["X", "O", " "], ["X", "X", "O"], ["O", "O", "X"]]
print(drawTable(3,board))
print(announceWinner(whoWins(board)))
