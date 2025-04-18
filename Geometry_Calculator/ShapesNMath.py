#Geometry Calculator Math File

from checkers import floatchecker, unitchecker

class Rectangle:

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def display_results(self, unit):
        area = self.area()
        perimeter = self.perimeter()
        print(f"\nThe area of the rectangle is: {area} {unit} squared and the perimeter is: {perimeter} {unit}.")

    def __init__(self):
        self.unit = unitchecker(input("\nWhat unit of measurement are you using?(Make sure it is like, mm, cm, in, ft, ect..)\n"))
        self.length = floatchecker(input("\nWhat is the length of the rectangle:\n"), "length")
        self.width = floatchecker(input("\nWhat is the width of the rectangle:\n"), "width")
        self.display_results(self.unit)
    
class Triangle:

    def area(self):
        return self.width * (self.height / 2)

    def perimeter(self, width):
        self.side2 = floatchecker(input("\nWhat is the length of the second side of the triangle:\n"), "second side")
        self.side3 = floatchecker(input("\nWhat is the length of the third side of the triangle:\n"), "third side")
        
        if self.width + self.side2 > self.side3 and self.width + self.side3 > self.side2 and self.side2 + self.side3 > self.width:
            return self.width + self.side2 + self.side3
        else:
            print("\nThat is not a valid triangle, try again.")
            self.perimeter(width)
            return self.width + self.side2 + self.side3
            

    def display_results(self, width, unit):
        area = self.area()
        perimeter = self.perimeter(width)
        print(f"\nThe area of the triangle is: {area} {unit} squared and the perimeter is: {perimeter} {unit}.")

    def __init__(self):
        self.unit = unitchecker(input("\nWhat unit of measurement are you using?(Make sure it is like, mm, cm, in, ft, ect..)\n"))
        self.height = floatchecker(input("\nWhat is the height of the triangle:\n"), "length")
        self.width = floatchecker(input("\nWhat is the width of the triangle:\n"), "width")
        self.display_results(self.width, self.unit)

class Circle:

    def area(self):
        return round(3.14159 * (self.radius ** 2), 2)

    def circumference(self):
        return round(2 * 3.14159 * self.radius, 2)

    def display_results(self, unit):
        area = self.area()
        circumference = self.circumference()
        print(f"\nThe area of the circle is: {area} {unit} squared and the circumference is: {circumference} {unit}.")

    def __init__(self):
        self.unit = unitchecker(input("\nWhat unit of measurement are you using?(Make sure it is like, mm, cm, in, ft, ect..)\n"))
        self.radius = floatchecker(input("\nWhat is the radius of the circle:\n"), "radius")
        self.display_results(self.unit)