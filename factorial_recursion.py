
def factorial( num ):
   if num <1:   # base case
       return 1
   else:
       return num * factorial( num - 1 )  # Recursive Call
for i in range(1,101,1 ):
    print("{}! = {}".format(i, factorial(i)))


