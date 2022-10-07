# Creating a List
webpages = ["Amazon", "google", "facebook"]

# get the first company name
print(webpages[0])

# get the second company name
print(webpages[1])

# try to get the fourth webpage name
# but this will return an error as only three names
# have been defined.


# To print entire list
print(webpages)

# Methods over PYTHON LISTS

# create an empty list
list1 = []

# add “Steve” to list1
list1.append("Steve")

# add "Jobs" to list1
list1.append("Jobs")

# print the items stored in list1
print(list1)

# insert “Lary” at position 1
list1.insert(1, "Lary")
# print the new list
print(list1)

# list.extend(another_list) - will add the elements in list 2 at the end of list (to concatinate 2 lists
langs = ["haskell", "clojure", "apl"]
langs.extend(["scala", "F#"])
print(langs)

# if you want to get the index of any element of the list
index_of_scala = langs.index("scala")
print(index_of_scala) # expected output is 3

# Removing elements from the lists
langs.remove("scala")
print(langs)


# assign a list to some_numbers
some_numbers = [5, 4, 3, 1]

# pop the list ( It will remove the last element)
some_numbers.pop()

# print the present list
print(some_numbers)

# pop the element at index 1
some_numbers.pop(1)



# Sorting of lists

# initialise an unsorted list some_numbers
some_numbers = [4,3,5,1]

# sort the list
some_numbers.sort()

# print the list to see if it is sorted.
print(some_numbers)

# To reverse a list
some_numbers.reverse()

# If you want the length of the list
print(len(some_numbers))

# get the sorted list
print(sorted(some_numbers))

# the original list remains unchanged
print(some_numbers)

# you have to assign  the sorted list to the original list to change it
some_numbers=some_numbers.sort()

print(some_numbers)




