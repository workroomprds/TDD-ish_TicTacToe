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
 --- ---
	"""
	assert( drawTable(1) == table11), "drawTable(1) produced "+drawTable(1)
	assert( drawTable(2) == table22), "drawTable(2) produced "+drawTable(2)
	
def drawRow(size):
	return("|   "*size+"|")

def drawDivider(size):
	return(" ---"*size)

def drawTable(size):
	table = "\n".join((drawDivider(1), drawRow(1), drawDivider(1)))
	return(table)

test() 
