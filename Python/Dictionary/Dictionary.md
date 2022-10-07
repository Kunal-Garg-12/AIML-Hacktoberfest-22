# Python Dictionaries

A dictionary is a set of unordered key, value pairs. In a dictionary, the keys must be unique and they are stored in an unordered manner.

### Refer to dictionary.py for code
## Creating a dictionary

 To create a dictionary you separate the key-value pairs by a colon(“:”). The keys would need to be of an immutable type, i.e., data-types for which the keys cannot be changed at runtime such as int, string, tuple, etc. The values can be of any type. Individual pairs will be separated by a comma(“,”) and the whole thing will be enclosed in curly braces({...}).
 (Check the code)
 Example: person_information = {'city': 'San Francisco', 'name': 'Sam', "food": "shrimps"}
 
## Get the values in a Dictionary
To get the values of a dictionary from the keys, you can directly reference the keys. To do this, you enclose the key in brackets [...] after writing the variable name of the dictionary.
 
You can also use the get method to retrieve the values in a dict. The only difference is that in the get method, you can set a default value. In direct referencing, if the key is not present, the interpreter throws KeyError.

## Add elements to a dictionary
You can add elements by updating the dictionary with a new key and then assigning the value to a new key.
Example: person1_information["Title"] = "Morgan" 

Or you can combine two dictionaries to get a larger dictionary using the update method.
Example: person1_information.update(<Other Dictionary>)
  
## Delete elements of a dictionary
To delete a key, value pair in a dictionary, you can use the del method.
A disadvantage is that it gives KeyError if you try to delete a nonexistent key.
  
So, instead of the del statement you can use the pop method. This method takes in the key as the parameter. As a second argument, you can pass the default value if the key is not present.
Example: print(person1_information.pop("food", None))  here "None" is the given as the default value that even if the doesn't exist it won't throw an error.
