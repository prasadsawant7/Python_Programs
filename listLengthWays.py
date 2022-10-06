# Python code to demonstrate
# length of list
# using naive method
 
# Initializing list
test_list = [1, 4, 5, 7, 8]
 
# Printing test_list
print("The list is : " + str(test_list))
 
# Finding length of list
# using loop
# Initializing counter
counter = 0
for i in test_list:
 
    # incrementing counter
    counter = counter + 1
 
# Printing length of list
print("Length of list using naive method is : " + str(counter))


a = []
a.append("Hello")
a.append("Geeks")
a.append("For")
a.append("Geeks")
print("The length of list is: ", len(a))


n = len([10, 20, 30])
print("The length of list is: ", n)
