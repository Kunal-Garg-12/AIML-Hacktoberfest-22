# Program that demonstrates usage and implementation of Functions

"""
    Why and What are functions?
    -> A block of organized code which is reusable to avoid same code redundancy.

    Syntax :
            def <function_name> (arguments...):
                /* Code Block*/
                return
                
    Types of Functions
    1. User defined functions
        => Functions that are defined by the User/programmer
    2. Predefined functions
        => Functions that are inbuilt
"""

# >== INBUILT FUNCTIONS ==<

# print() => Displays data on the console
print("Hello World")  # Displays "Hello World" on the console, and returns None
# Displays "Programming is Life" on the console, and returns None
print("Programming is life")

# abs() => Accepts a number and returns a absolute value of the number
value1 = abs(-2)  # Returns 2
print(value1)  # Displays 2
value2 = abs(35)  # Returns 35
print(value2)  # Displays 35


# >== USER DEFINED FUNCTION ==<

# Simple demonstration of Function, that accepts a name (string) and returns a greeting (string)
def greet(name="User"): # Default value of name is "User" if not passed
    string = f"Hello {name},\nWelcome to Python Programming we will be discussing about functions()\n"
    return string


# Example : greet(name)
print(greet("Alexa")) # Displays the text with Alexa as name
print(greet()) # Uses default name as User


# Function that finds the factorial value of a number
# Concept used : Recursion
# Recursion - It is method of calling the same function within it, until reaches the specified condition
def factorial(number):
    if(number == 0):  # Terminating condition - checking if number value is 0
        return 1
    else:
        # Multiplying the current number with return value of present function passing value one less
        return number * factorial(number - 1)


# Example : factorial(number)
print(factorial(7)) # Displays 5040
print(factorial(10)) # Displays 3628800


# Callback function
def callbackfunction1(string):  # Callback function 1
    print(f"Thank you! {string}\n")


def callbackfunction2(string):  # Callback function 2
    print(f"Your Welcome! {string}\n")


def assign(name, role, callback):  # Accept parameters name (string), role (string), callback (function)
    print(f"Hello {role},")
    print("Hope you are enjoying")
    callback(name)  # Function Callback


# Example : assign(name, role, callback)
assign("John", "Developer", callbackfunction1) # Callback function 1
assign("Alexa", "Designer", callbackfunction2) # Callback function 2


# Function with n number of arguments
def calculatesum(*args):
    total = 0
    for value in args:
        total += value
    return total


# Example : calculatesum(*args)
print(calculatesum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) # Output 55
print(calculatesum(2, 4, 5, 6, 20)) # Output 37


# Lambda Functions
def cube(x): return x ** 3  # Lambda function to find cube of a number


# Example : cube(x)
print(cube(3)) # Output 27
print(cube(7)) # Output 343
