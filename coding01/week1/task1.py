task1.py


"""a programe that outputs odd / even numbers - if a number at all"""


while True:
	try:
		answer=float(input("what is your number?: "))
		if answer % 2 == 0:
			print("even number")
		else:	
			print("odd number")
		except ValueError:
			print("not a number")	