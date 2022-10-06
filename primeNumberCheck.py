# Program to check if a number is prime or not

# Get input from the user
numberinput = int(input("Enter a number: "))

# prime numbers are greater than 1
if numberinput > 1:
    # check if number input is a prime number
    if (numberinput % 2) == 0:
        print(numberinput, "is not a prime number")
    else:
        print(numberinput, "is a prime number")