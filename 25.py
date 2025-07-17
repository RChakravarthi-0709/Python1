import random as rd

list1 = list("abcdefghijklmnopqrstuvwxyz")
list2 = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
list3 = list("1234567890")

rand1 = rd.randint(0, len(list1)-1)
rand2 = rd.randint(0, len(list2)-1)
rand3 = rd.randint(0, len(list3)-1)

pwd = list1[rand1] + list2[rand2] + list3[rand3]
print(pwd)