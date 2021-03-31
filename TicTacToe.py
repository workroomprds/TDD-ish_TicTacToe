#!/usr/bin/env python3

def test():
	assert( drawRow(3) == "|   |   |   |")
	assert( drawDivider(3) == " --- --- ---")
	table11 = """ ---
|   |
 ---"""
	table22 = """ --- ---
|   |   |
 --- ---
|   |   |
 --- ---"""
	assert( drawTable(1) == table11), "drawTable(1) produced "+drawTable(1)
	assert( drawTable(2) == table22), "drawTable(2) produced "+drawTable(2)
	
def drawRow(size):
	return("|   "*size+"|")

def drawDivider(size):
	return(" ---"*size)

def drawTable(size):
	def addTopAndCentre(target,numberOfColumns):
		target.append(drawDivider(numberOfColumns))
		target.append(drawRow(numberOfColumns))
	
	def addBottomRow(target, numberOfColumns):
		target.append(drawDivider(numberOfColumns))
	
	def joinRowsWithNewLine(target):
		return("\n".join(target))
	
	collection = []
	for i in range(size):
		addTopAndCentre(collection, size)
	addBottomRow(collection, size)
	
	return(joinRowsWithNewLine(collection))

test() 
print(drawTable(10))