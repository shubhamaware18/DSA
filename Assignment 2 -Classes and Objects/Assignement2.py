# Assignement 2 - Objects and Class

# Q1. Define a python class Person with instance object variables name and age. Set Instance object variables in _init_() method. Also define show() method to display name and age of a person.
class Person:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        # Display the name and age of the person
        print(f"Name: {self.name}, Age: {self.age}")

person1 = Person("Alice", 30)
person1.show()

person2 = Person("Bob", 25)
person2.show()

#===========================================================================================================================================================#
# Q2. Define a class Circle with instance object variable radius. Provide setter and getter for radius. Also define getArea() and getCircumference() methods.
class Circle:
    # instance 
    def __init__(self, radius):
        self.radius = radius

    # setter function
    def set_radius(self, radius):
        self.radius = radius
    
    # getter funcction
    def get_radius(self):
        return f"The Radius of Circle is {self.radius}"
    
    # function for area
    def getArea(self):
        return f"The Area of Circle is {3.14 * (self.radius ** 2)}"
    
    def getCircumference(self):
        return f"The Circumference of the Circle is {2 * 3.14 * self.radius}"
    
obj = Circle(35)
print(obj.get_radius())
print(obj.getArea())
print(obj.getCircumference())
    
#===========================================================================================================================================================#
# Q3. Define a class Rectangle with length and breadth as instance object variables. Provide setDimensions(), showDimensions() and getArea() method in it.
# Q4. Define a class Book with instance object variables bookid, title and price. Initialise them via_init_() method. Also define method to show book variables.
# Q5. Define a class Team with instance object variable a list of team member names. Provide methods to input member names and display member names.