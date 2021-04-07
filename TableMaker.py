#!/usr/bin/env python3

class TableMaker():
	defaultTableHeaders = ["1", "2", "3", "4", "5", "6", "7", "8", "9"] #single chars onle
	defaultRowLabels = ["A", "B", "C", "D", "E", "F", "G", "H", "I"] #single chars only
	
	def __init__(self, size= 3, headerLabels=defaultTableHeaders, rowLabels=defaultRowLabels):
		self.size =    size
		self.rowLabels =    rowLabels
		self.headerLabels = headerLabels
		
	def drawTable(self, content=[]):		
		if (content !=[]):
			def drawRow(rowNumber):
				return(self.drawFilledRow(self.rowLabels[rowNumber], self.size, content[rowNumber]))
		else:
			def drawRow(rowNumber):
				return( self.drawEmptyRow(self.rowLabels[rowNumber], self.size) )
			
		myDivider = self.drawDivider(self.size) # one of these
		myColumnLabels = self.makeHeaderRow(self.size, self.headerLabels) # one of these
		rows = list(map(drawRow, range(self.size))) ## a list with as many rows as needed
		
		return(self.joinRowsWithNewLine(self.buildRowsIntoList(myColumnLabels, myDivider, rows)))
	
	def drawEmptyRow(self, rowInfo, size):
		return(rowInfo+" "+"|   "*size+"|")
	
	def drawFilledRow(self, rowInfo, size, content):
		collection = [rowInfo+" "+"|"]
		for i in range(size):
			collection.append(" "+content[i]+" |")
		return("".join(collection))
	
	def drawDivider(self, size):
		return("  "+" ---"*size)
	
	def makeHeaderRow(self, numberOfColumns, contents):
		return("    "+"   ".join(contents[0:numberOfColumns]))
	
	def joinRowsWithNewLine(self, target):
		return("\n".join(target))
	
	def buildRowsIntoList(self, headerLabels, divider, rows):
		collection = []
		collection.append( headerLabels )
		collection.append( divider )
		for row in rows:
			collection.append( row )
			collection.append( divider )
		return(collection)


def test():
	
	t = TableMaker(2)
	
	# test routines to draw header, divider, empty and filled row, building tabls as a list, joining list with newline
	assert( t.makeHeaderRow(2, ["1", "2"]) == "    1   2"), "produced "+ t.makeHeaderRow(2, ["1", "2"]) 
	assert( t.drawEmptyRow("A",3) ==  "A |   |   |   |"), "produced "+t.drawRow("A",3) 
	assert( t.drawDivider(3) == "   --- --- ---")
	assert( t.drawFilledRow("A", 2, ["X", "O"]) =="A | X | O |")
	assert( t.buildRowsIntoList("Labels", "Divider", ["Row1", "Row2"]) == ["Labels", "Divider", "Row1", "Divider", "Row2", "Divider"])
	assert( t.joinRowsWithNewLine(["A", "b"]) == """A
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
	
	testTableMaker1 = TableMaker(1)
	testTableMaker2 = TableMaker(2)
	testTableMaker = TableMaker()
	drawTable = testTableMaker.drawTable
	
	assert( testTableMaker1.drawTable() == table11)
	assert( testTableMaker2.drawTable() == table22)
	assert ( drawTable(dataForFilledTable33) == filledTable33) # done as 'approval test'
	
	testTableMaker4 = TableMaker(size=2, rowLabels = ["X", "Y"], headerLabels=["!","?"] )
	#specialisedLabels = {"rowLabels":["X", "Y"], "headerLabels":["!","?"]}
	emptyTableDiffHeaders22 = """    !   ?
   --- ---
X |   |   |
   --- ---
Y |   |   |
   --- ---"""
	#print(testTableMaker4.drawTable())
	assert ( testTableMaker4.drawTable() == emptyTableDiffHeaders22) # done as 'approval test'
	
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
	
	
test() 
