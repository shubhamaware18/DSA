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
class Rectangle:
    # constructor
    def __init__(self, length=0, breadth=0):
        self.length = length
        self.breadth = breadth

    # setter
    def setDimensions(self,length, breadth):
        self.length = length
        self.breadth = breadth

    # showDimensions()
    def showDimensions(self):
        return f"Length of Rectange is: {self.length} and Breadth is: {self.breadth}"
    
    # get area
    def getArea(self):
        return f"Area of Rectange is: {self.length * self.breadth}"
    
obj = Rectangle()
obj.setDimensions(10, 5)
print(obj.showDimensions())
print(obj.getArea())
        
#===========================================================================================================================================================#
# Q4. Define a class Book with instance object variables bookid, title and price. Initialise them via_init_() method. Also define method to show book variables.

class Book:
    def __init__(self, bookid, title, price):
        self.bookid = bookid
        self.title = title
        self.price = price
        
    
    def showDetails(self):
        # Display the details of the book
        print(f"Book ID: {self.bookid}, Title: {self.title}, Price: ${self.price}")

book1 = Book(1, "The Great Gatsby", 10.99)
book1.showDetails()  

book2 = Book(2, "1984", 8.99)
book2.showDetails()  

#===========================================================================================================================================================#
# Q5. Define a class Team with instance object variable a list of team member names. Provide methods to input member names and display member names.

class Team:
    def __init__(self):
        self.members = []

    def addMember(self, name):
        self.members.append(name)

    def showMembers(self):
        # Display the names of the team members
        if self.members:
            print("Team Members:")
            for member in self.members:
                print(f"- {member}")
        else:
            print("No members in the team.")

team = Team()
team.addMember("Alice")
team.addMember("Bob")
team.addMember("Charlie")
team.showMembers()