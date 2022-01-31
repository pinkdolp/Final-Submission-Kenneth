a = 1
b = 1

def fibonacci(a, b, iterations):
	print(a)
	print(b)
	for i in range(0, iterations):
		c = a + b
		a = b
		b = c
		print(c)

#fibonacci(a,b,5)

def fibonacci_recursive(a, b, generation, count=0):
		

		if count =< iterations:
			return b

		else:
			
			return fibonacci_recursive(b, a + b,count+1)

print(a)
for i in range(0,10):
	print(fibonacci_recursive(a,b,i))