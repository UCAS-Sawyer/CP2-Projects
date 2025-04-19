# Geometry Calculator Math File for Rectangles

# Import necessary modules
from checkers import floatchecker, unitchecker
import matplotlib.pyplot as plt

class Rectangle:
    # Method to calculate the area of the rectangle
    def area(self):
        return self.length * self.width

    # Method to calculate the perimeter of the rectangle
    def perimeter(self):
        return 2 * (self.length + self.width)

    # Method to display the results (area, perimeter, and shape)
    def display_results(self):
        self.area_measurement = self.area()
        self.perimeter_length = self.perimeter()
        self.showshape()  # Display the rectangle shape

    # Method to visualize the rectangle using matplotlib
    def showshape(self):
        # Create a rectangle using matplotlib
        fig, ax = plt.subplots()
        rectangle = plt.Rectangle((0, 0), self.length, self.width, edgecolor='blue', facecolor='lightblue')
        ax.add_patch(rectangle)
        ax.set_xlim(0, self.length + 1)
        ax.set_ylim(0, self.width + 1)
        ax.set_aspect('equal', adjustable='box')
        plt.title("Graph Rectangle")
        plt.xlabel("Length")
        plt.ylabel("Width")
        plt.grid(True)
        # Display area and perimeter inside the rectangle
        plt.text(self.length / 2, self.width / 2, f"Area: {self.area_measurement} {self.unit}\nPerimeter: {self.perimeter_length} {self.unit}", color="black", ha="center", va="center", fontsize=10, bbox=dict(facecolor='white', alpha=0.5))
        plt.show()

    # Constructor to initialize the rectangle object
    def __init__(self):
        #inputs
        self.unit = unitchecker(input("\nWhat unit of measurement are you using?(Make sure it is like, mm, cm, in, ft, etc..)\n"))
        self.length = floatchecker(input("\nWhat is the length of the rectangle?\n"), "length")
        self.width = floatchecker(input("\nWhat is the width of the rectangle?\n"), "width")

        # Display the results
        self.display_results()