count = 100
cells = [] # True means cell is open/prisoner released early
lucky = []
unlucky = []
for i in range(0, count, 1): # opening position
    cells.append(False)
for j in range(0, count, 1): # in parameters, the end represents rounds
    for i in range(j, count, j+1): # Round 1
        if cells[i] == True:
            cells[i] = False
        else:
            cells[i] = True

for i in range(0, count, 1):
    if cells[i] == True:
        lucky.append(i+1)
    else:
        unlucky.append(i+1)
print(lucky)
print(unlucky)