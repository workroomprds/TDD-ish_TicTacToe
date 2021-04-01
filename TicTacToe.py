#!/usr/bin/env python3

def test():
	
	assert( makeHeaderRow(2, ["1", "2"]) == "    1   2"), "produced "+ makeHeaderRow(2, ["1", "2"]) 
	assert( drawEmptyRow("A",3) ==  "A |   |   |   |"), "produced "+drawRow("A",3) 
	assert( drawDivider(3) == "   --- --- ---")
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
	testTableMaker = TableMaker()
	drawTable = testTableMaker.drawTable
	
	assert( drawTable(1) == table11), "drawTable(1) produced "+drawTable(1)
	assert( drawTable(2) == table22), "drawTable(2) produced "+drawTable(2)
	
	assert( joinRowsWithNewLine(["A", "b"]) == """A
b""")
	assert (drawFilledRow("A", 2, ["X", "O"]) =="A | X | O |")
	
	dataForFilledTable33 = [["X", "O", " "], ["X", "X", "O"], ["O", "O", "X"]]
	filledTable33 = """    1   2   3
   --- --- ---
A | X | O |   |
   --- --- ---
B | X | X | O |
   --- --- ---
C | O | O | X |
   --- --- ---"""
	
	assert ( drawTable(3, dataForFilledTable33) == filledTable33) # done as 'approval test'
	
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

class TableMaker():
	def __init__(self):
		myHeaders = ""
		
	def drawTable(self, size, content=[]):
		def drawRow(): #untested - depends on plenty from inside fn
			return(drawFilledRow(rowLabels[i], size, content[i]) if (full) else drawEmptyRow(rowLabels[i], size) )
		rowLabels =    ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
		headerLabels = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
		full = content !=[]
		myDivider = drawDivider(size)
		myColumnLabels = makeHeaderRow(size, headerLabels)
		
		collection = []
		collection.append(myColumnLabels)
		collection.append( myDivider )
		for i in range(size):
			collection.append( drawRow() )
			collection.append( myDivider )
		return(joinRowsWithNewLine(collection))
	


test() 

myTableMaker = TableMaker()
print(myTableMaker.drawTable(9))
#print(drawTable(3, [["X", "O", " "], ["X", "X", "O"], ["O", "O", "X"]]))
#print(drawTable(3))