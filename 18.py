import random as rd
upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P","Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list1 = []
all = upper + lower + nums
def genPwd1(size):
    pwd = []
    digit1 = rd.randint(0, 25)
    pwd.append(upper[digit1])
    digit1 = rd.randint(0, 25)
    pwd.append(lower[digit1])
    digit1 = rd.randint(0, 9)
    pwd.append(str(nums[digit1]))
    for i in range(0, size-3, 1):
        digit1 = rd.randint(0,61)
        pwd.append(str(all[digit1]))
    rd.shuffle(pwd)
    pwd1 = ''.join(pwd)
    return pwd1

def genPwd2(size, quantity):
    password = ""
    for i in range(0, quantity, 1):
        password = genPwd1(size)
        list1.append(password)
    return list1
param1 = 5
param2 = 10
list1 = genPwd2(param1, param2)
print(list1)