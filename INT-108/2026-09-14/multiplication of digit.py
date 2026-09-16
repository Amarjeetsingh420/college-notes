n = int(input())
s = 1
for i in range(0,len(str(n))):
    s *= n%10 
    n = n//10
print(s)