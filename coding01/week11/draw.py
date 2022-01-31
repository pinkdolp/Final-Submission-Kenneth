from polygon import Polygon,Square

triangle = Polygon(sides=3, length=100)
square = Square( length=100)

#triangle.draw()
#square.draw()

print("Perimeter: {}, Area: {}".format(square.perimeter(), square.area() )