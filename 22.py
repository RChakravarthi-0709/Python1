from mod_17 import fileDetails
schools = ["KV", "DPS"]
scores_KV = fileDetails("marks_KV.txt")
scores_DPS = fileDetails("marks_DPS.txt")
for i in range(0, 5, 1):
    if scores_KV[2][i] > scores_DPS[2][i]:
        print(f"The top scorer in {scores_KV[0][i]} is {scores_KV[1][i]} from {schools[0]} with marks {scores_KV[2][i]}")
    elif scores_KV[2][i] == scores_DPS[2][i]:
        print(f"The top scorer in {scores_KV[0][i]} is a tie between {scores_KV[1][i]} from {schools[0]} and {scores_DPS[1][i]} from {schools[1]} with marks {scores_KV[2][i]}")
    else:
        print(f"The top scorer in {scores_KV[0][i]} is {scores_DPS[1][i]} from {schools[1]} with marks {scores_DPS[2][i]}")
if scores_KV[3] > scores_DPS[3]:
    print(f"The gold medalist is {scores_KV[5][scores_KV[4]]} from {schools[0]} with marks {scores_KV[3]}")
elif scores_KV[3] == scores_DPS[3]:
    print(f"The gold medalist is a tie between {scores_KV[5][scores_KV[4]]} from {schools[0]} and {scores_DPS[5][scores_DPS[4]]} from {schools[1]} with marks {scores_KV[3]}")
else:
    print(f"The gold medalist is {scores_DPS[5][scores_DPS[4]]} from {schools[1]} with marks {scores_DPS[3]}")