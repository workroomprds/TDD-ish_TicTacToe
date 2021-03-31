#!/usr/bin/env python3

def test():
	assert( drawRow(3) == "|   |   |   |")
	assert( drawDivider(3) == " --- --- ---")
	
def drawRow(size):
	return("|   "*size+"|")

def drawDivider(size):
	return(" ---"*size)

test() 