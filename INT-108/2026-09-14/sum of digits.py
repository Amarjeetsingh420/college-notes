n = int(input())
s = 0
for i in range(0,len(str(n))):
   r = n%10
   s += r
   n = n//10
print(s)