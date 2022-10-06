# Method 1
lst=[ 1, 6, 3, 5, 3, 4 ]
#checking if element 7 is present
# in the given list or not
i=7
# if element present then return
# exist otherwise not exist
if i in lst:
    print("exist")
else:
    print("not exist")


# Method 2
# Initializing list
test_list = [10, 15, 20, 7, 46, 2808]
 
print("Checking if 15 exists in list")
 
# number of times element exists in list
exist_count = test_list.count(15)
 
# checking if it is more then 0
if exist_count > 0:
    print("Yes, 15 exists in list")
else:
    print("No, 15 does not exists in list")


# Method 3
from bisect import bisect_left ,bisect
 
# Initializing list
test_list_set = [ 1, 6, 3, 5, 3, 4 ]
test_list_bisect = [ 1, 6, 3, 5, 3, 4 ]
 
print("Checking if 4 exists in list ( using set() + in) : ")
 
# Checking if 4 exists in list
# using set() + in
test_list_set = set(test_list_set)
if 4 in test_list_set :
    print ("Element Exists")
 
print("Checking if 4 exists in list ( using sort() + bisect_left() ) : ")
 
# Checking if 4 exists in list
# using sort() + bisect_left()
test_list_bisect.sort()
if bisect_left(test_list_bisect, 4)!=bisect(test_list_bisect, 4):
    print ("Element Exists")
else:
    print("Element doesnt exist")


# Method 4
# Initializing list
test_list = [10, 15, 20, 7, 46, 2808]
 
print("Checking if 15 exists in list")
x=list(map(str,test_list))
y="-".join(x)
 
if y.find("15") !=-1:
    print("Yes, 15 exists in list")
else:
    print("No, 15 does not exists in list")


# Method 5
from collections import Counter
 
test_list = [10, 15, 20, 7, 46, 2808]
 
# Calculating frequencies
frequency = Counter(test_list)
 
# If the element has frequency greater than 0
# then it exists else it doesn't exist
if(frequency[15] > 0):
    print("Yes, 15 exists in list")
else:
    print("No, 15 does not exists in list")
