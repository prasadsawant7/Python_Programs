def negativenumbers(a,b):
  # Checking condition for negative numbers
  # single line solution
  out=[i for i in range(a,b+1) if i<0]
  # print the all negative numbers
  print(*out)
 
# driver code
# a -> start range
a=-4
# b -> end range
b=5
negativenumbers(a,b)
