# Geometry Calculator Math File for seeing existing shapes

import csv

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
        # Method to view all shapes in the CSV file

        with open("Geometry_Calculator/Shapes.csv", "r") as file:
            reader = csv.reader(file)
            print("\nAll Shapes:")
            for row in reader:
                if row[0] == "Rectangle":
                    print(f"\nShape: {row[0]}, Length: {row[1]} {row[5]}, Width: {row[2]} {row[5]}, Area: {row[3]} {row[5]}², Perimeter: {row[4]} {row[5]}")
                elif row[0] == "Triangle":
                    print(f"\nShape: {row[0]}, Side1: {row[1]} {row[6]}, Side2: {row[2]} {row[6]}, Side3: {row[3]} {row[6]}, Area: {row[4]} {row[6]}², Perimeter: {row[5]} {row[6]}")
                elif row[0] == "Circle":
                    print(f"\nShape: {row[0]}, Radius: {row[1]} {row[4]}, Area: {row[2]} {row[4]}², Circumference: {row[3]} {row[4]}")