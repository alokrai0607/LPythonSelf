def sumOfN(n):
   if(n<=0):
     return 0
   return n + sumOfN(n-1)

a  = sumOfN(10)
print(a)