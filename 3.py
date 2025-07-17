num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
for j in range(num1, num2+1, 1):
    for i in range(1, 11, 1):
        print(j, i, j*i)
    print()