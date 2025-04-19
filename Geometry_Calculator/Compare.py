# Geometry Calculator Math File for Comparing Shapes

from checkers import int_checker  # Importing int_checker function from checkers module

class compare_shapes:

    def Rectangle(self):
        # Method to calculate area and perimeter of a rectangle
        self.length = float(input("\nEnter the length of the rectangle:\n"))
        self.width = float(input("\nEnter the width of the rectangle:\n"))

        self.area = self.length * self.width
        self.perimeter = 2 * (self.length + self.width)

        return self.area, self.perimeter, "Rectangle"
    
    def Triangle(self): 
        # Method to calculate area and perimeter of a triangle
        self.base = float(input("\nEnter the base of the triangle: \n"))
        self.height = float(input("\nEnter the height of the triangle: \n"))
        self.side2 = float(input("\nEnter the length of the second side: \n"))
        self.side3 = float(input("\nEnter the length of the third side: \n"))

        # Check if the sides form a valid triangle
        if self.base + self.side2 > self.side3 and self.base + self.side3 > self.side2 and self.side2 + self.side3 > self.base:
            self.area = 0.5 * self.base * self.height
            self.perimeter = self.base + self.side2 + self.side3
            return self.area, self.perimeter, "Triangle"
        else:
            print("\nThe sides entered do not form a valid triangle.")
            return self.Triangle()  # Restart triangle input
    
    def Circle(self):
        # Method to calculate area and circumference of a circle
        self.radius = float(input("\nEnter the radius of the circle: \n"))

        self.area = round(3.14159 * (self.radius ** 2), 2)    
        self.circumference = round(2 * 3.14159 * self.radius, 2)

        return self.area, self.circumference, "Circle"
    
    def compare_shapes_func(self):
        # Method to compare two shapes
        self.shape1 = []
        self.shape2 = []

        # Get the first shape
        self.shape1_type = input("\nEnter the type of the first shape 1. Rectangle, 2: Triangle, 3. Circle\n").strip()

        if self.shape1_type == "1":
            self.shape1 = self.Rectangle()
        elif self.shape1_type == "2":
            self.shape1 = self.Triangle()
        elif self.shape1_type == "3":
            self.shape1 = self.Circle()
        else:
            print("\nThat is not an option.")
            self.compare_shapes_func()  # Restart the comparison process

        # Get the second shape
        self.shape2_type = input("\nEnter the type of the second shape 1. Rectangle, 2: Triangle, 3. Circle\n").strip()

        if self.shape2_type == "1":
            self.shape2 = self.Rectangle()
        elif self.shape2_type == "2":
            self.shape2 = self.Triangle()
        elif self.shape2_type == "3":
            self.shape2 = self.Circle()
        else:
            print("\nThat is not an option.")
            self.compare_shapes_func()
        
        # Print area and perimeter comparisons
        print(self.compare_area())
        print(self.compare_perimeter())

    def compare_area(self):
        # Method to compare areas of two shapes
        area1 = self.shape1[0]
        area2 = self.shape2[0]
        if area1 > area2:
            return f"\nShape1, {self.shape1[2]}, has a larger area."
        elif area1 < area2:
            return f"\nShape2, {self.shape2[2]}, has a larger area."
        else:
            return "\nBoth shapes have the same area."

    def compare_perimeter(self):
        # Method to compare perimeters of two shapes
        perimeter1 = self.shape1[1]
        perimeter2 = self.shape2[1]
        if perimeter1 > perimeter2:
            return f"\nShape1, {self.shape1[2]}, has a larger perimeter."
        elif perimeter1 < perimeter2:
            return f"\nShape2, {self.shape2[2]}, has a larger perimeter."
        else:
            return "\nBoth shapes have the same perimeter."
        
    def Sort_shapes(self):
        # Method to sort multiple shapes by area or perimeter
        number_of_shapes = int_checker(input("\nHow many shapes do you want to compare?\n"))
        self.shapes = []
        for x in range(number_of_shapes):
            # Get each shape
            shape_type = input("\nEnter the type of shape 1. Rectangle, 2: Triangle, 3. Circle\n").strip()

            if shape_type == "1":
                self.shapes.append(self.Rectangle())
            elif shape_type == "2":
                self.shapes.append(self.Triangle())
            elif shape_type == "3":
                self.shapes.append(self.Circle())
            else:
                print("\nThat is not an option.")
                self.Sort_shapes()  # Restart the sorting process
            
        # Sort shapes by area or perimeter
        sort_by = input("\nDo you want to sort by 1. area or 2. perimeter?\n").strip()

        if sort_by == "1":
            self.shapes.sort(key=lambda x: x[0])
            print(f"\nThe shapes sorted by area: {self.shapes}")
        elif sort_by == "2":
            self.shapes.sort(key=lambda x: x[1])
            print(f"\nThe shapes sorted by perimeter: {self.shapes}")
        else:
            print("\nThat is not an option.")
            self.Sort_shapes()

    def __init__(self):
        # Constructor to start the program
        coice = input("\nWhat would you like to do, 1: Compare Shapes, 2: Sort Shapes?\n")
        
        if coice == "1":
            self.compare_shapes_func()

        elif coice == "2":
            self.Sort_shapes()

        else:
            compare_shapes()  # Restart the process if invalid choice