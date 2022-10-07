# Python program to print Even Numbers in a given range

first = int(input("Enter the first number of the range: "))
last = int(input("Enter the last number of the range: "))

print("The even numbers in your specified range is: ")

# iterating each number in list
for num in range(first, last + 1):

	# checking condition
	if num % 2 == 0:
		print(num, end=" ")
print("")
