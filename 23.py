list1 = []
list2 = []
list3 = []
for i in range(0, 26, 1):
    list1.append(chr(i+65))
    list2.append(chr(i+97))
for i in range(0, 10, 1):
    list3.append(i)
list4 = list1 + list2 + list3
print(list4)