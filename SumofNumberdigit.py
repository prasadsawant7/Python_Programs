n=int(input("Enter the size of the list"))
lst=[]

print("Enter the values in the list")
for i in range(0,n):
    ele=int(intput())
    lst.append(ele)
print("Original list : "+str(lst))
ans=[]
for ele in lst:
    sum=0
    for dig in str(ele):
        sum+=int(dig)
    ans.append(sum)
print("The Sum of Number Digit in list is :"+str(ans))