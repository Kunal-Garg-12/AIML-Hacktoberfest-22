# Creating a dictionary
person_information = {'city': 'San Francisco', 'name': 'Sam', "food": "shrimps"}

type(person1_information) # to get the datatype (Expected output: <class 'dict'>)

print(person1_information)


# To get the values in a Dictionary
print(person1_information["city"])

# Using get method
alphabets = {1:'a'} # create a small dictionary
print(alphabets.get(1))  # get the value with key 1

# get the value with key 2. Pass “default” as default. Since key 2 does not exist, you get “default” as the return value.
print(alphabets.get(2, "default"))


# Add elements to a dictionary

# initialize an empty dictionary
person1_information = {}

# add the key, value information with key “city”
person1_information["city"] = "San Francisco"
# print the present person1_information
print(person1_information)

# add another key, value information with key “name”
person1_information["name"] = "Sam"
# print the present dictionary
print(person1_information)

# Combining two dictionaries

# have a different dictionary
remaining_information = {'name': 'Sam', "food": "shrimps"}

# add the second dictionary remaining_information to personal1_information using the update method
person1_information.update(remaining_information)

# print the current dictionary
print(person1_information) #Expected output: "{'city': 'San Francisco', 'name': 'Sam', 'food': 'shrimps'}"


#Delete elements of a Dictionary

# delete the key, value pair with the key “food”.
del person1_information["food"]

# print the present personal1_information.
print(person1_information) #Expected output: "{'city': 'San Francisco', 'name': 'Sam'}"

# remove a key, value pair with key “food” and default value None using pop.
print(person1_information.pop("food", None)) #This will not show an error even if the key does not exist


# Checking if a key is present

alphabets = {1:'a'} # Expected: "True"
alphabets.has_key(1) # Expected: "False"

