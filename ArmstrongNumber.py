#Given a number x, determine whether the given number is Armstrong number or not.
#  A positive integer of n digits is called an Armstrong number of order n (order is number of digits) if.
#abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + .... 

def isArmstrong(x):
     
    n = len(str(x)) #here n is the order of the number
    temp = x
    sum1 = 0
     
    while (temp != 0):
        r = temp % 10
        sum1 = sum1 + r**n
        temp = temp // 10
 
    # If condition satisfies
    return (sum1 == x)
 
# Driver code
x = 153
print(isArmstrong(x))
 
x = 1253
print(isArmstrong(x))