f1 = open("marks.txt", "r")
list1 = []
students = []
sub1 = []
toppersSub1 = []
subjects = []

for i in range(0, 26, 1):
    s1 = f1.readline()
    list1 = s1.split(",")
    students.append(list1[0])
    list2 = list1[3].split(":")
    subjects.append(list2[0])
    sub1.append(list2[1])
maxSub1 = max(sub1)
print(students)
print(sub1)
print(maxSub1)
for i in range(0, 26, 1):
    if sub1[i] == maxSub1:
        toppersSub1.append(students[i])
    print(toppersSub1, "are the toppers in", subjects[0], "with marks", maxSub1)