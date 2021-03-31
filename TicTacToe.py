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
	
def drawEmptyRow(rowInfo, size):
	return(rowInfo+" "+"|   "*size+"|")

def drawDivider(size):
	return("  "+" ---"*size)

def makeHeaderRow(numberOfColumns, contents):
	return("    "+"   ".join(contents[0:numberOfColumns]))

def joinRowsWithNewLine(target):
	return("\n".join(target))

def drawTable(size):
	# note - no tests for these
	
	rowLabels =    ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
	headerLabels = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
	collection = [makeHeaderRow(size, headerLabels)]
	for i in range(size):
		collection.append(drawDivider(size))
		collection.append(drawEmptyRow(rowLabels[i], size))
	collection.append(drawDivider(size))
	
	return(joinRowsWithNewLine(collection))

test() 

print(drawTable(9))