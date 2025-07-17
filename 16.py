f1 = open("marks_DPS.txt", "r")
list1 = []
students = []
subjects = []
sub1 = []
sub2 = []
sub3 = []
sub4 = []
sub5 = []
subs = [sub1, sub2, sub3, sub4, sub5]
toppersSub1 = []
toppersSub2 = []
toppersSub3 = []
toppersSub4 = []
toppersSub5 = []
toppersSubs = [toppersSub1, toppersSub2, toppersSub3, toppersSub4, toppersSub5]
totalScores = [0] * 26


for i in range(0, 26, 1):
    s1 = f1.readline()
    list1 = s1.split(",")
    students.append(list1[0])
    for j in range(3, 8, 1):
        list2 = list1[j].split(":")
        subjects.append(list2[0])
        subs[j-3].append(int(list2[1]))
        totalScores[i] += int(list2[1])
maxSub1 = max(sub1)
maxSub2 = max(sub2)
maxSub3 = max(sub3)
maxSub4 = max(sub4)
maxSub5 = max(sub5)
maxSubs = [maxSub1, maxSub2, maxSub3, maxSub4, maxSub5]
for i in range(0, 26, 1):
    for j in range(0, 5, 1):
        if subs[j][i] == maxSubs[j]:
            toppersSubs[j].append(students[i])
topScore = 0
topperPosition = 0
for i in range(0, 26, 1):
    if totalScores[i] > topScore:
        topScore = totalScores[i]
        topperPosition = i
for i in range(0, 5, 1):
    print(toppersSubs[i], "are the toppers in", subjects[i], "with marks", maxSubs[i])
print(students[topperPosition], "is the gold medalist with", topScore, "marks")