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
	def addTopAndCentre(collection,size):
		collection.append(drawDivider(size))
		collection.append(drawRow(size))
	
	def addBottomRow(collection, size):
		collection.append(drawDivider(size))
	
	def joinRowsWithNewLine(collection):
		return("\n".join(collection))
	
	collection = []
	for i in range(size):
		addTopAndCentre(collection, size)
	
	addBottomRow(collection, size)
	return(joinRowsWithNewLine(collection))

test() 
