"""Bitwise Operators in Python
a) Bitwise AND (&): This operator performs a logical AND operation on each pair of corresponding bits of two integers. The result is 1 if both bits are 1, otherwise, it is 0.
b) Bitwise OR (|): This operator performs a logical OR operation on each pair of corresponding bits of two integers. The result is 1 if at least one of the bits is 1, otherwise, it is 0.
c) Bitwise XOR (^): This operator performs a logical XOR operation on each pair of corresponding bits of two integers. The result is 1 if the bits are different, otherwise, it is 0.
Example:"""
a = int(input("Enter a value: "))
b = int(input("Enter another value: "))
print("a & b =", a & b)
print("a | b =", a | b)
print("a ^ b =", a ^ b)