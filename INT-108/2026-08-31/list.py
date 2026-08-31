l1 = [1, 2, 3, 4, 5]
l2 =["hello", "world"]
l1[-1] = "bye"
print("list after changing last element:", l1)
l2.append("hello")
l2.append(12.56)
print("list after adding new element:", l2)
print(l1 + l2)
print("length of list l1:", len(l1))
print("length of list l2:", len(l2))
print("l1*2:", l1*2)
print(l1[0:3:2])
