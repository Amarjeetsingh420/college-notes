a = int(input())
if(a<0):
    print("Please enter the non-negative number")
elif(a==0):
    print("factorial of Zero is 1")
else:
    i = 1
    fact = 1
    while(i<a):
        i += 1
        fact *= i
    print("factorial of" ,a ,"is",fact)