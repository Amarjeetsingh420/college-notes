n = int(input("Enter a non-negative number: "))
if(n<0):
    print("Please enter a positive number")
elif(n==0 or n==1):
    print("fib at",n,"is",n)
else:
    a = 0
    b = 1
    i = 2
    while(i<=n):
        a,b = b, a+b
        i += 1
    print(b)