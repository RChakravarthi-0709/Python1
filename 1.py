num1 = []
num2 = []
for i in range(3, 21):
    num1.append(i)

for i in range(1, 11):
    num2.append(i)

for i in range(0, len(num1), 1):
    for x in range(0, len(num2), 1):
        total = num1[i]*num2[x]
        print(num1[i], " * ", num2[x], " = ", total)