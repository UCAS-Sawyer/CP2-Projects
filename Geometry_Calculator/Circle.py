#Geometry Calculator Math File for Circles

from checkers import floatchecker, unitchecker
import matplotlib.pyplot as plt
import csv

class Circle:
    # Calculate the area of the circle
    def area(self):
        return round(3.14159 * (self.radius ** 2), 2)

    # Calculate the circumference of the circle
    def circumference(self):
        return round(2 * 3.14159 * self.radius, 2)
    
    # Static method to explain the formulas
    @staticmethod
    def explain_formulas():
        return "Area = π × radius², Circumference = 2 × π × radius"

    # Display the results (area, circumference, and shape)
    def display_results(self):
        self.area_measurement = self.area()
        self.circumference_length = self.circumference()
        # Display the explanation of formulas
        print(self.explain_formulas())

        with open("Geometry_Calculator/Shapes.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Circle", self.radius, self.area_measurement, self.circumference_length, self.unit])

        self.showshape()

    # Visualize the circle using matplotlib
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
        plt.title(f"Circle: Radius={self.radius} {self.unit}")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid(True)

        # Add area, circumference, and radius as text
        plt.text(self.radius, self.radius + self.radius * 0.5, f"Area: {self.area_measurement} {self.unit}\nCircumference: {self.circumference_length} {self.unit}", color="black", ha="center", va="center", fontsize=10, bbox=dict(facecolor='white', alpha=0.5))
        plt.text(self.radius * 1.5, self.radius + 0.2, f"Radius: {self.radius} {self.unit}", color="blue", fontsize=10)

        # Show the plot
        plt.show()

    # Initialize the Circle object with user input
    def __init__(self):
        # Get the unit of measurement from the user
        self.unit = unitchecker(input("\nWhat unit of measurement are you using?(Make sure it is like, mm, cm, in, ft, ect..)\n"))
        # Get the radius of the circle from the user
        self.radius = floatchecker(input("\nWhat is the radius of the circle:\n"), "radius")

        # Display the results
        self.display_results()
