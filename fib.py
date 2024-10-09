#0,1,1,2,3,5,7,12........

def fib(n):
   a = 0
   b = 1
   print(a)
   print(b)
   for i in range(2,n-1): #Iterate from 2 to n +1 because 0 and 1 were printed
       c = a + b
       a = b
       b = c
       print(c)
   return a + b

print(fib(100))
