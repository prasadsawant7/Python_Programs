# list of numbers
list1 = [-10, -21, -4, 45, -66, 93]
 
# using list comprehension
pos_nos = [num for num in list1 if num >= 0]
 
print("Positive numbers in the list: ", *pos_nos)
