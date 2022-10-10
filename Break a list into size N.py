my_list = ['college', 'office', 'google', 'code',
           'microsoft','cloud', 'Machine learning', 'python'
               'java', 'life']
 
# Yield successive n-sized
# chunks from l.
def divide_chunks(l, n):
     
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]
 
# How many elements each
# list should have
n = 5
 
x = list(divide_chunks(my_list, n))
print (x)
