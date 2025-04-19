# Geometry Calculator Math File for Triangles

# Import necessary modules
from checkers import floatchecker, unitchecker
import matplotlib.pyplot as plt
import csv

class Triangle:

    # Method to calculate the area of the triangle using Heron's formula
    def area(self):
        s = (self.width + self.side2 + self.side3) / 2  # Semi-perimeter
        return round((s * (s - self.width) * (s - self.side2) * (s - self.side3)) ** 0.5, 2)

    # Method to calculate the perimeter of the triangle
    def perimeter(self):
        return self.width + self.side2 + self.side3
    
    @staticmethod
    def explain_formulas():
        return (
            "\nArea = √[s(s-a)(s-b)(s-c)], where s = (a + b + c) / 2 (Heron's formula)\n"
            "Perimeter = a + b + c"
        )

    # Method to display the results (area, perimeter, and shape)
    def display_results(self):
        self.area_measurement = self.area()  # Calculate area
        self.perimeter_length = self.perimeter()  # Calculate perimeter

        with open("Geometry_Calculator/Shapes.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Triangle", self.width, self.side2, self.side3, self.area_measurement, self.perimeter_length, self.unit])
        
        self.showshape()  # Display the triangle shape

    # Method to plot and display the triangle shape
    def showshape(self):
        # Calculate the coordinates of the second vertex
        x2, y2 = self.width, 0  # Second vertex (width along the x-axis)

        # Calculate the x and y coordinates of the third vertex using the law of cosines
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
        plt.title(f"Triangle: Sides={self.width} {self.unit}, {self.side2} {self.unit}, {self.side3} {self.unit}")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid(True)

        # Add area, perimeter, and height as text
        plt.text(self.width / 2, y3 / 3, f"Area: {self.area_measurement} {self.unit}\nPerimeter: {self.perimeter_length} {self.unit}", 
                color="black", ha="center", va="center", fontsize=10, bbox=dict(facecolor='white', alpha=0.5))
        plt.text(x3 + 0.2, y3 / 2, f"Height: {round(y3, 2)} {self.unit}", color="blue", fontsize=10)  # Label the height

        # Show the plot
        plt.show()

    # Constructor to initialize the triangle and validate its sides
    def __init__(self):
        # Get the unit of measurement
        self.unit = unitchecker(input("\nWhat unit of measurement are you using?(Make sure it is like, mm, cm, in, ft, etc..)\n"))
        
        # Get the lengths of the three sides
        self.width = floatchecker(input("\nWhat is the length of the first side of the triangle (base):\n"), "base")
        self.side2 = floatchecker(input("\nWhat is the length of the second side of the triangle:\n"), "second side")
        self.side3 = floatchecker(input("\nWhat is the length of the third side of the triangle:\n"), "third side")
        
        # Check if the triangle is valid
        if self.width + self.side2 > self.side3 and self.width + self.side3 > self.side2 and self.side2 + self.side3 > self.width:
            # Display the explanation of formulas
            print(self.explain_formulas())

            self.display_results()  # Display results if the triangle is valid
        else:
            print("\nThe side lengths do not make a triangle. Try again.")
            Triangle()  # Restart the process if the triangle is invalid
