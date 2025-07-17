f1 = open("in2.txt", "r")
num1 = int(f1.readline())
num2 = int(f1.readline())
for j in range(num1, num2+1, 1):
    for i in range(1, 11, 1):
        print(j, i, j*i)
    print()