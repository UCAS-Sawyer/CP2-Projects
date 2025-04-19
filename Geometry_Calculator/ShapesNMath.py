#Geometry Calculator Math File

from checkers import floatchecker, unitchecker
import matplotlib.pyplot as plt

class Rectangle:

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def display_results(self):
        self.area_measurement = self.area()
        self.perimeter_length = self.perimeter()
        self.showshape()

    def showshape(self):
        # Create a rectangle using matplotlib
        fig, ax = plt.subplots()
        rectangle = plt.Rectangle((0, 0), self.length, self.width, edgecolor='blue', facecolor='lightblue')
        ax.add_patch(rectangle)
        ax.set_xlim(0, self.length + 1)
        ax.set_ylim(0, self.width + 1)
        ax.set_aspect('equal', adjustable='box')
        plt.title(f"Rectangle: {self.length}{self.unit} x {self.width}{self.unit}")
        plt.xlabel("Length")
        plt.ylabel("Width")
        plt.grid(True)
        plt.text(self.length / 2, self.width / 2, f"Area: {self.area_measurement}{self.unit}\nPerimeter: {self.perimeter_length}{self.unit}", color="black", ha="center", va="center", fontsize=10, bbox=dict(facecolor='white', alpha=0.5))
        plt.show()

    def __init__(self):
        self.unit = unitchecker(input("\nWhat unit of measurement are you using?(Make sure it is like, mm, cm, in, ft, ect..)\n"))
        self.length = floatchecker(input("\nWhat is the length of the rectangle:\n"), "length")
        self.width = floatchecker(input("\nWhat is the width of the rectangle:\n"), "width")
        self.display_results()


class Triangle:

    def area(self):
            # Use Heron's formula to calculate the area
            s = (self.width + self.side2 + self.side3) / 2  # Semi-perimeter
            return round((s * (s - self.width) * (s - self.side2) * (s - self.side3)) ** 0.5, 2)

    def perimeter(self):
            return self.width + self.side2 + self.side3
            

    def display_results(self):
        self.area_measurement = self.area()
        self.perimeter_length = self.perimeter()
        self.showshape()

    def showshape(self):
        # Calculate the coordinates of the third vertex using the law of cosines
        x2, y2 = self.width, 0  # Second vertex (width along the x-axis)
        # Calculate the x and y coordinates of the third vertex
        cos_angle = (self.width**2 + self.side3**2 - self.side2**2) / (2 * self.width * self.side3)
        x3 = self.side3 * cos_angle
        y3 = (self.side3**2 - x3**2) ** 0.5  # Pythagorean theorem for height

        # Plot the triangle
        fig, ax = plt.subplots()
        triangle = plt.Polygon([(0, 0), (x2, y2), (x3, y3)], edgecolor='green', facecolor='lightgreen')
        ax.add_patch(triangle)

        # Plot the height as a dashed line
        ax.plot([x3, x3], [0, y3], color='blue', linestyle='--', linewidth=2)  # Dashed line for height

        # Set plot limits and aspect ratio
        ax.set_xlim(0, max(self.width, x3) + 1)
        ax.set_ylim(0, y3 + 1)
        ax.set_aspect('equal', adjustable='box')

        # Add title, labels, and grid
        plt.title(f"Triangle: Sides={self.width}{self.unit}, {self.side2}{self.unit}, {self.side3}{self.unit}")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid(True)

        # Add area, perimeter, and height as text
        plt.text(self.width / 3, y3 / 3, f"Area: {self.area_measurement}{self.unit}\nPerimeter: {self.perimeter_length}{self.unit}", 
                 color="black", ha="center", va="center", fontsize=10, bbox=dict(facecolor='white', alpha=0.5))
        plt.text(x3 + 0.2, y3 / 2, f"Height: {round(y3, 2)}{self.unit}", color="blue", fontsize=10)  # Label the height

        # Show the plot
        plt.show()

    def __init__(self):
        self.unit = unitchecker(input("\nWhat unit of measurement are you using?(Make sure it is like, mm, cm, in, ft, etc..)\n"))
        self.width = floatchecker(input("\nWhat is the length of the first side of the triangle (base):\n"), "base")
        self.side2 = floatchecker(input("\nWhat is the length of the second side of the triangle:\n"), "second side")
        self.side3 = floatchecker(input("\nWhat is the length of the third side of the triangle:\n"), "third side")
        # Check if the triangle is valid
        if self.width + self.side2 > self.side3 and self.width + self.side3 > self.side2 and self.side2 + self.side3 > self.width:
            self.display_results()
        else:
            print("\nThe side lengths do not make a triangle. Try again.")
            Triangle()


class Circle:

    def area(self):
        return round(3.14159 * (self.radius ** 2), 2)

    def circumference(self):
        return round(2 * 3.14159 * self.radius, 2)

    def display_results(self):
        self.area_measurement = self.area()
        self.circumference_length = self.circumference()
        self.showshape()

    def showshape(self):
        # Create a circle using matplotlib
        fig, ax = plt.subplots()
        circle = plt.Circle((self.radius, self.radius), self.radius, edgecolor='red', facecolor='pink')
        ax.add_patch(circle)

        # Plot the radius as a line
        ax.plot([self.radius, self.radius * 2], [self.radius, self.radius], color='blue', linestyle='--', linewidth=2)

        # Set plot limits and aspect ratio
        ax.set_xlim(0, self.radius * 2 + 1)
        ax.set_ylim(0, self.radius * 2 + 1)
        ax.set_aspect('equal', adjustable='box')

        # Add title, labels, and grid
        plt.title(f"Circle: Radius={self.radius}{self.unit}")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid(True)

# Add area, circumference, and radius as text
        # Move the area and circumference text box slightly upward
        plt.text(self.radius, self.radius + self.radius * 0.5, f"Area: {self.area_measurement}{self.unit}\nCircumference: {self.circumference_length}{self.unit}", color="black", ha="center", va="center", fontsize=10, bbox=dict(facecolor='white', alpha=0.5))
        plt.text(self.radius * 1.5, self.radius + 0.2, f"Radius: {self.radius}{self.unit}", color="blue", fontsize=10)

        # Show the plot
        plt.show()

    def __init__(self):
        self.unit = unitchecker(input("\nWhat unit of measurement are you using?(Make sure it is like, mm, cm, in, ft, ect..)\n"))
        self.radius = floatchecker(input("\nWhat is the radius of the circle:\n"), "radius")
        self.display_results()