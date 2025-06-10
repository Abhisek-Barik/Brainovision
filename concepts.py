# IMPORTS
# VARIABLES
a = 1
b = "hi"
c = 1.5
# CONDITIONAL CONTROLS
if a > 0:
    print("a is positive")
else:
    print("a is not positive")
print(b)
# LOOPS
for i in range(2,5,2):
    print(f"Loop iteration {i}")
# FUNCTIONS
def greet(name):
    return f"Hello, {name}!"
# FUNCTION CALL
print(greet("Alice"))
# MODULES
import math
def calculate_circle_area(radius):
    return math.pi * radius ** 2
# FUNCTION CALL
print(f"Area of circle with radius 3: {calculate_circle_area(3)}")

from ops import add, subtract, multiply, divide
print(subtract(2, 3))  # Should print 5

# LISTS
my_list = [1, 2, 3, 4, 5]
# LIST OPERATIONS
my_list[2] = 10  # Update element at index 2
my_list.append(6)
my_list.remove(2)
# PRINT LIST
print("Updated list:", my_list)
# TUPLES
my_tuple = (1, 2, 3)
# TUPLE OPERATIONS
print("Tuple elements:", my_tuple)
# DICTIONARIES
my_dict = {"name": "Alice", "age": 30}
# DICTIONARY OPERATIONS
my_dict["city"] = "New York"
my_dict["age"] += 1  # Increment age
# PRINT DICTIONARY
print("Updated dictionary:", my_dict)
# SETS
my_set = {1, 2, 3}
# SET OPERATIONS
my_set.add(4)
# PRINT SET
print("Updated set:", my_set)
k = input("Enter a number: ")
j = input("Enter another number: ")
print(f"Sum of {k} and {j}: {add(k, j)}")  # Should print the sum of k and j

# STRINGS
my_string = "Hello, World!"
# STRING OPERATIONS
my_string_upper = my_string.upper()  # Convert to uppercase 
print("Uppercase string:", my_string_upper)
# STRING FORMATTING
formatted_string = f"{my_string} - Length: {len(my_string)}"
print("Formatted string:", formatted_string)

# CLASSES
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
# CLASS USAGE
person = Person("Bob", 25)
print(person.greet())

# ABSTRACTION
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method.")
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
class Square(Shape):    
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2
# ABSTRACTION USAGE
circle = Circle(3) 
print(circle.radius)  # Should print 3
print(f"Area of circle: {circle.area()}")
square = Square(4)
print(f"Area of square: {square.area()}")
# ENCAPSULATION
class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def get_balance(self):
        return self.__balance
# ENCAPSULATION USAGE
account = BankAccount(100)
# print(account.__balance)
print(f"Initial balance: {account.get_balance()}")
account.deposit(50)
print(f"Balance after deposit: {account.get_balance()}")
account.withdraw(30)
print(f"Balance after withdrawal: {account.get_balance()}")
# POLYMORPHISM
class Animal:
    def speak(self):
        raise NotImplementedError("Subclasses must implement this method.")
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"
# POLYMORPHISM USAGE
def animal_sound(animal):
    print(animal.speak())
dog = Dog()
cat = Cat()
animal_sound(dog)  # Should print "Woof!"
animal_sound(cat)  # Should print "Meow!"
# INHERITANCE
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def info(self):
        return f"Vehicle Make: {self.make}, Model: {self.model}"
class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.doors = doors

    def info(self):
        return f"{super().info()}, Doors: {self.doors}"
# INHERITANCE USAGE
car = Car("Toyota", "Corolla", 4)
print(car.info())  # Should print vehicle info with doors
# FILE I/O
with open("example.txt", "w") as file:
    file.write("Hello, File I/O!")
# FILE I/O READ
with open("example.txt", "r") as file:
    content = file.read()
    print("File content:", content)  # Should print "Hello, File I/O!"
# EXCEPTIONS
try:
    result = divide(10, 0)  # This will raise an exception
except ValueError as e:
    print(f"Error: {e}")
# EXCEPTIONS HANDLING
try:
    result = divide(10, 2)  # This will not raise an exception
    print(f"Division result: {result}")
# EXCEPTIONS HANDLING
except ValueError as e:
    print(f"Error: {e}")