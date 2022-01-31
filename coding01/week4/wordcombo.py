"""wordcombo.py"""

import re

input = input("enter word here: ")

input = re.split(', / , /; / ; / - / - /' ,input)

for x in input:
	if not x.isalpha():
		print("only alphabetic words!")
		quit()

for x in range(0, len(input)):
	for y in range(len(input)-1, x, -1):
		print(input[x] + " " + input[y])

		
