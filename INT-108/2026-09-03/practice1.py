n=input("Enter a character: ")
if(ord(n)>=65 and ord(n)<=90) or (ord(n)>=97 and ord(n)<=122):
    if(n in "AEIOU"):
        print("yes, it is a vowel")
    else:
        print("no, it is not a vowel")
else:
    print("please enter a valid character")
