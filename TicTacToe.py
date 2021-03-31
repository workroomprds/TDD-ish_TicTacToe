#!/usr/bin/env python3

def test():
	assert( drawRow(2) == "|   |   |")
	assert( drawDivider(2) == " --- ---")
	
def drawRow(size):
	return("|   "*size+"|")

def drawDivider(size):
	return(" ---"*size)

test() 