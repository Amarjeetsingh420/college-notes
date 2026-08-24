a = int(input("Enter a value: "))
b = int(input("Enter another value: "))
print("before swapping:","a is", a, "b is", b)
a = a^b
b = a^b
a = a^b
print("after swapping:","a is", a, "b is", b)
