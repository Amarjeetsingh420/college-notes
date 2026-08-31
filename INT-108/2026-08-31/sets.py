s1 = {1, 2, 3, 4, 5}
s2 = {"hello", "world"}
print("set s1:", s1)
print("set s2:", s2)
#sets are unordered, so we cannot change elements
print("length of set s1:", len(s1))
print("length of set s2:", len(s2))
#sets are mutable, so we can add new elements
s1.add(6)
s2.add("python")
print("set s1 after adding new element:", s1)
print("set s2 after adding new element:", s2)
#creating a set with single element
s3 = {1}
print("set s3:", s3)
print("length of set s3:", len(s3))
#creating an empty set
s4 = set()
print("set s4:", s4)
print("length of set s4:", len(s4))