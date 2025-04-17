#Geometry Calculator Math File

from checkers import floatchecker

class Rectangle:

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def display_results(self):
        area = self.area()
        perimeter = self.perimeter()
        print(f"\nThe area of the rectangle is: {area} and the perimeter is: {perimeter}.")

    def __init__(self):
        self.length = floatchecker(input("\nWhat is the legnth of the rectangle:\n"), "length")
        self.width = floatchecker(input("\nWhat is the width of the rectangle:\n"), "width")
        self.display_results()
    


def Triangle():
    print("YLO")

def Circle():
    print("YLO")