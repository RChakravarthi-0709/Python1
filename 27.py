import random as rd


list1 = list("abcde6!$@f2ghijklmnopqr*#^(#*stuvwxyz#DEFGHI&#^JKLMNOPQR#S$@!VWXYZ1234567890")
def genPwd1(length, dataset):
    pswd = ""
    for _ in range(0, length, 1):
        rand1 = rd.randint(0, len(list1) - 1)
        pswd += dataset[rand1]
    return pswd
def genPwd2(length, quantity, dataset):
    pwds = []
    for _ in range(0, quantity, 1):
        pwds.append(genPwd1(length, list1))
    return pwds
print(genPwd2(9, 4, list1))