list1 = []
list2 = []
for i in range(0, 26, 1):
    list1.append(chr(i+65))
print(list1)
for i in range(0, 26, 1):
    list2.append(ord(list1[i]))
print(list2)