a = str(input("enter a value: "))
b = " is odd"
c = " is even"
d = "is neither odd or even"
for element in a:
	if element == '.' or element.isalpha():
		print(a + d)
		quit()
	if (int(a) % 2 == 0):
	print(a + c)
else:
print(a + b)		