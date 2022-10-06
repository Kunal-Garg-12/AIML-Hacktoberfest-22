#INTRO ---------------------------------------------------------------------------------------------------
#Object-Oriented Programming (OOP) in Python
#Object-oriented programming is a simple feature that provides a means of structuring programs so that properties and behaviors are bundled into individual objects.


# Defining a Class in Python.
# Why do we need a class in first place ?
# Let's say you are given a task to track an employ of a company, you will need to store some basic information such as name, age, salary etc.
# One approach is to represent each employee as list but it will just lsrger your code and make it more complex.
# The easier approach to this issue is to use a class.

# So now,how to define a class ?

class employee:
    pass

# This a very basic class named as "employee" we used pass keyword as it allows you to run this code without Python throwing an error.

# Objects
#The object is an entity that has a state and behavior associated with it. It may be any real-world object like a mouse, keyboard, chair etc.


#Creating an object -

obj = employee()


#The properties that all employee objects must have are defined in a method called .__init__().
#Let’s update the employee class with an .__init__() method that creates .name and .age attributes:

class employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#In the body of .__init__(), there are two statements using the self variable:
   #self.name = name creates an attribute called name and assigns to it the value of the name parameter.
   #self.age = age creates an attribute called age and assigns to it the value of the age parameter.


# Creating Class and objects with methods -

class employee:
 
    # class attribute
    attr1 = "male"
 
    # Instance attribute
    def __init__(self, name):
        self.name = name
         
    def speak(self):
        print("My name is {}".format(self.name))
 
# Driver code
# Object instantiation
Rohan = employee("Rohan")
Tushar = employee("Tushar")
 
# Accessing class methods
Rohan.speak()
Tushar.speak()


# Inheritance
# Inheritance is the capability of one class to derive or inherit the properties from another class. 
# Example of inheritance in python -

# parent class
class Bird:
    
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()

# We created two classes i.e. Bird (parent class) and Penguin (child class). The child class inherits the functions of parent class.


#Encapsulation
#Using OOP in Python, we can restrict access to methods and variables.
#Data Encapsulation in Python

class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()

# In the above program, we defined a Computer class.
# We used __init__() method to store the maximum selling price of Computer.


#Polymorphism
#Polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types).
#Suppose, we need to color a shape, there are multiple shape options (rectangle, square, circle). 
#However we could use the same method to color any shape. This concept is called Polymorphism.

#Using Polymorphism in Python -

class Parrot:

    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

class Penguin:

    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")

# common interface
def flying_test(bird):
    bird.fly()

#instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)


#In the above program, we defined two classes Parrot and Penguin. Each of them have a common fly() method.
#However, their functions are different.
