# Geometry Calculator Math File for seeing existing shapes

import csv
from checkers import int_checker
import matplotlib.pyplot as plt

class View_shapes:
    def __init__(self):
        choice = input("\nWould you like to 1. View All Shapes, 2. View Selected Shape?\n").strip()
        if choice == "1":
            self.view_all_shapes()
        elif choice == "2":
            self.view_selected_shape()
        else:
            print("\nThat is not an option.")
            self.View_shapes()  # Restart the view process

    def view_all_shapes(self):
        x = 0
        # Method to view all shapes in the CSV file

        with open("Geometry_Calculator/Shapes.csv", "r") as file:
            reader = csv.reader(file)
            print("\nAll Shapes:")
            for row in reader:
                x += 1
                if row[0] == "Rectangle":
                    print(f"\n{x}. Shape: {row[0]}, Length: {row[1]} {row[5]}, Width: {row[2]} {row[5]}, Area: {row[3]} {row[5]}², Perimeter: {row[4]} {row[5]}")
                elif row[0] == "Triangle":
                    print(f"\n{x}. Shape: {row[0]}, Side1: {row[1]} {row[6]}, Side2: {row[2]} {row[6]}, Side3: {row[3]} {row[6]}, Area: {row[4]} {row[6]}², Perimeter: {row[5]} {row[6]}")
                elif row[0] == "Circle":
                    print(f"\n{x}. Shape: {row[0]}, Radius: {row[1]} {row[4]}, Area: {row[2]} {row[4]}², Circumference: {row[3]} {row[4]}")
    
    def view_selected_shape(self):
        self.view_all_shapes()
        choice = int_checker(input("\nEnter the number of the shape you want to view:\n")) - 1

        with open("Geometry_Calculator/Shapes.csv", "r") as file:
            reader = csv.reader(file)
            shapes = list(reader)  # Convert the CSV reader object to a list of rows
            if 0 <= choice <= len(shapes)-1:  # Ensure the choice is within bounds
                shape = shapes[choice]
            else:
                print("\nInvalid selection. Please try again.")
        if shape[0] == "Rectangle":
            self.length = float(shape[1])
            self.width = float(shape[2])
            self.area_measurement = float(shape[3])
            self.perimeter_length = float(shape[4])
            self.unit = shape[5]
            
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
        
        elif shape[0] == "Triangle":
            self.width = float(shape[1])
            self.side2 = float(shape[2])
            self.side3 = float(shape[3])
            self.area_measurement = float(shape[4])
            self.perimeter_length = float(shape[5])
            self.unit = shape[6]

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
        
        elif shape[0] == "Circle":
            
            self.radius = float(shape[1])
            self.area_measurement = float(shape[2])
            self.circumference_length = float(shape[3])
            self.unit = shape[4]

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


