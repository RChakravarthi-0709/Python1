f1 = open("in3.txt", "r")
s1 = f1.readline()
list1 = s1.split(",")
num1 = int(list1[0])
num2 = int(list1[1])
for j in range(num1, num2+1, 1):
    for i in range(1, 11, 1):
        print(j, i, j*i)
    print()