a = int(input("Enter your a: "))
b = int(input("Enter your b: "))
c = int(input("Enter your c: "))

if(a>b and a>c):
    print(a, "a is greatest number among all of the three")
elif(b>a and b>c):
    print(b ,"b is greatest number among all of the three")
else:
    print(c,"c is greatest number among all of the three")