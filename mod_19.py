import random as rd
import string as string
list1 = []
ascii = string.ascii_letters + string.digits
def genPwd1(size):
    pwd = []
    digit1 = rd.randint(65, 91)
    pwd.append(chr(digit1))
    digit1 = rd.randint(97, 122)
    pwd.append(chr(digit1))
    digit1 = rd.randint(0, 9)
    pwd.append(str(digit1))
    for i in range(0, size-3, 1):
        digit1 = rd.randint(0,61)
        pwd.append(ascii[digit1])
    rd.shuffle(pwd)
    pwd1 = ''.join(pwd)
    return pwd1

def genPwd2(size, quantity):
    password = ""
    for i in range(0, quantity, 1):
        password = genPwd1(size)
        list1.append(password)
    return list1