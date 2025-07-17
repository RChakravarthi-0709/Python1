import random as rd


list1 = list("abcde6!$@f2ghijklmnopqr*#^(#*stuvwxyz#DEFGHI&#^JKLMNOPQR#S$@!VWXYZ1234567890")
def genpswd(length, dataset):
    pswd = ""
    for _ in range(0, length, 1):
        rand1 = rd.randint(0, len(list1) - 1)
        pswd += dataset[rand1]
    return pswd

print(genpswd(9, list1))