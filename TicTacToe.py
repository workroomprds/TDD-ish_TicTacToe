#!/usr/bin/env python3

def test():
	assert( drawRow(3) == "|   |   |   |")
	assert( drawDivider(3) == " --- --- ---")
	table11 = """ ---
|   |
 ---"""
	assert( drawTable(1) == table11), "produced "+drawTable(1)
	
def drawRow(size):
	return("|   "*size+"|")

def drawDivider(size):
	return(" ---"*size)

def drawTable(size):
	table = "\n".join((drawDivider(1), drawRow(1), drawDivider(1)))
	return(table)

test() 
