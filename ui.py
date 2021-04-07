#!/usr/bin/env python3

import utils

def askForInput(request):
	return(input(request))

def output(stuff):
	print(stuff)
	
def announceWinner(winner):
	return(winner+" wins!" if (winner!="Draw") else "Draw")

def build_input_request(player:str, desiredInputs:list)->str:
	"""Returns string to ask player to input location"""
	return ("".join(("Place ",player," in space ",utils.return_list_of_values_separated_by_slashes(desiredInputs)," : ")))


def request_valid_input(player:str, validSet:list, get_input:object)->str:
	"""Returns a valid choice within the rules - choce from function (typically input)"""
	#validSet = valid_input_for_game(rules)
	request = build_input_request(player, validSet)
	choice = ""
	while not (utils.accept_input(validSet, choice) ):
		choice = get_input(request)
	return(choice)

def test():
	def test_Winner():
		assert (announceWinner("Q") == "Q wins!")
		assert (announceWinner("Draw") == "Draw")
		
	def test_build_input_request():
		assert (build_input_request("X", ["A", "B", "C"])=="Place X in space A / B / C : ")
		
	test_Winner()
	test_build_input_request()
	
test()