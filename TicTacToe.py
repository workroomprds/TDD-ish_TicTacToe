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
	assert( drawTable(1) == table11), "drawTable(1) produced "+drawTable(1)
	assert( drawTable(2) == table22), "drawTable(2) produced "+drawTable(2)
	
	assert( joinRowsWithNewLine(["A", "b"]) == """A
b""")
	assert (drawFilledRow("A", 2, ["X", "O"]) =="A | X | O |")
	
	filledTable = """    1   2   3
   --- --- ---
A | X | O |   |
   --- --- ---
B | X | X | O |
   --- --- ---
C | O | O | X |
   --- --- ---"""
	
	assert ( drawFilledTable(3, [["X", "O", " "], ["X", "X", "O"], ["O", "O", "X"]]) == filledTable) # done as 'approval test'
	
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

def drawTable(size):
	rowLabels =    ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
	headerLabels = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
	collection = [makeHeaderRow(size, headerLabels)]
	for i in range(size):
		collection.append(drawDivider(size))
		collection.append(drawEmptyRow(rowLabels[i], size))
	collection.append(drawDivider(size))
	
	return(joinRowsWithNewLine(collection))

def drawFilledTable(size, content):
	# refactor later
	rowLabels =    ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
	headerLabels = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
	drawRow = drawFilledRow
	collection = [makeHeaderRow(size, headerLabels)]
	for i in range(size):
		collection.append(drawDivider(size))
		collection.append(drawRow(rowLabels[i], size, content[i]))
	collection.append(drawDivider(size))
	return(joinRowsWithNewLine(collection))

test() 

print(drawTable(9))
print(drawFilledTable(3, [["X", "O", " "], ["X", "X", "O"], ["O", "O", "X"]]))