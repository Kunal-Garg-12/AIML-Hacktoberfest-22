# Lists
A list is a data-structure, or it can be considered a container that can be used to store multiple data at once. The list will be ordered and there will be a definite count of it. The elements are indexed according to a sequence and the indexing is done with 0 as the first index. Each element will have a distinct place in the sequence and if the same value occurs multiple times in the sequence, each will be considered separate and distinct element.

To create a list, you separate the elements with a comma and enclose them with a bracket “[]”. Check the Lists.py for actual code.

To access any element of the list "List_name[<index>]".
  
## Methods over Python Lists
Python lists support common methods that are commonly required while working with lists. The methods change the list in place. In case you want to make some changes in the list and keep both the old list and the changed list, take a look at the functions that are described after the methods.

### How to add elements to the list:
list.append(elem) - will add another element to the list at the end. 
Note the items are printed in the order in which they youre inserted.
  
list.insert(index, element) - will add another element to the list at the given index, shifting the elements greater than the index one step to the right. In other words, the elements with the index greater than the provided index will increase by one.

list.extend(<another_list>) - will add the elements in list 2 at the end of list.
  
list.index(<element>) - will give the index number of the element in the list.

### How to remove elements from thee List:
  
list.remove(<element>) - will search for the first occurrence of the element in the list and will then remove it.

list.pop() - will remove the last element of the list. If the index is provided, then it will remove the element at the particular index. For example, if you have a list [5, 4, 3, 1] and you apply the method pop, it will return the last element 1 and the resulting list will not have it.

### Sorting of list:
  
list.sort() - will sort the list in-place.
  
### Reversing a list:

list.reverse() - will reverse the list in place.
  
## Functions over Python Lists:
  
You use the function “len” to get the length of the list.
  
If you use another function “enumerate” over a list, it gives us a nice construct to get both the index and the value of the element in the list.
  For example, you have the list of companies ['Amazon', 'google', 'facebook'] and you want the index, along with the items in the list, you can use the enumerate function.
  
 sorted function will sort over the list.
 Similar to the sort method, you can also use the sorted function which also sorts the list. The difference is that it returns the sorted list, while the sort method sorts the list in place. So this function can be used when you want to preserve the original list as well.
  
