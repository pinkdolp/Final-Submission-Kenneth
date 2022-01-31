 func_lists.py

 try:
 	num1 = int(input("enter a number: "))
 	num2 = int(input("enter a second number: "))
 	num3 = int(input('enter a third number: '))
 	num4 = int(input("enter a fourth number: "))

 except ValueError as e:
 print("that is not a valid integer")

 n_list = [num1, num2, num3, num4]

 def multiply (n_list):
 	x = lambda a, b, c, d: a * b * c * d
 	print(x(n_list[0], n_list[1], n_list[2], n_list[3]))

 multiply(n_list)	