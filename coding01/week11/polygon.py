import turtle	
t = turtle.Turtle()

class Polygon:
	sides = 0
	length = 0

	def __init__(self,sides,length):
		self.sides = sides
		self.length = length

		def draw(self):
			internal_angle = self.__internal_angle()

			for _ in range(0,self.sides):
				t.forward(self.length)
				t.right(180 - internal_angle)


			turtle.done()

		def perimeter(self):
				return self.sides*self.length	

		def area(self):
			a = 0
			j = self.sides -1

			for i in range(0, self.sides):				
		
		def __internal_angle(self):		
			return ((self.sides -2) * 180) / self.sides

class Square(Polygon):		
	def __init__(self, length):
		super().__init__(sides=4, length=length)

	def area(self):
		return self.length ** 2

class Triangle(Polygon):
	def __init__(self, length):
		super().__init__(sides=3, length=length)			

