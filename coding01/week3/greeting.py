"""greeting.py"""

def name(first, second = ""):
	if second == "":
		print("hey" + first + "how are u?")
	else: print("nice to meet you" + first + " " + second + " ")

first = input("first name: ")
second = input("second name: ")

name(first, second)	
