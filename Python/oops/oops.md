
**PLEASE NOTE** KINDLY REFER TO [oops.py] TO UNDERSTAND THE WORKING OF ALL THESE CONCEPTS WHEN USED IN A PYTHON PROGRAM.

# Object-Oriented Programming (OOP) in Python

# What Is Object-Oriented Programming in Python?

--> Object-oriented programming is a programming paradigm that provides a means of structuring programs so that properties and behaviors are bundled into individual objects.

For instance, an object could represent a person with properties like a name, age, and address and behaviors such as walking, talking, breathing, and running. Or it could represent an email with properties like a recipient list, subject, and body and behaviors like adding attachments and sending.
The key takeaway is that objects are at the center of object-oriented programming in Python, not only representing the data, as in procedural programming, but in the overall structure of the program as well.

# Define a Class in Python

--> Primitive data structures—like numbers, strings, and lists—are designed to represent simple pieces of information, such as the cost of an apple, the name of a poem, or your favorite colors, respectively. What if you want to represent something more complex?

For example, let’s say you want to track employees in an organization. You need to store some basic information about each employee, such as their name, age, position, and the year they started working.
**One way to do this is to represent each employee as a list but there are a number of issues with this approach.**
--> A great way to make this type of code more manageable and more maintainable is to use classes.

# Class
--> A class is a blueprint for the object.
--> We can think of class as a sketch of a parrot with labels. It contains all the details about the name, colors, size etc. Based on these descriptions, we can study about the parrot. Here, a parrot is an object.

# Object
--> An object (instance) is an instantiation of a class. When class is defined, only the description for the object is defined. Therefore, no memory or storage is allocated.

# Methods
--> Methods are functions defined inside the body of a class. They are used to define the behaviors of an object.

# Inheritance
--> Inheritance is a way of creating a new class for using details of an existing class without modifying it. The newly formed class is a derived class (or child class). Similarly, the existing class is a base class (or parent class).

# Encapsulation
--> Using OOP in Python, we can restrict access to methods and variables. This prevents data from direct modification which is called encapsulation. In Python, we denote private attributes using underscore as the prefix i.e single _ or double __.

# Polymorphism
--> Polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types).
--> Suppose, we need to color a shape, there are multiple shape options (rectangle, square, circle). However we could use the same method to color any shape. This concept is called Polymorphism.