sodou = []
for i in range(9):
    s = [int(i) for i in input().split()]
    sodou.append(s)
    
test = []
for i in sodou:
    add1 = 0
    for j in range(9):
        add1 += i[j]
    if add1 != 45:
        test.append(1)
        break

for i in range(9):
    add2 = 0
    for j in range(9):
        add2 += sodou[j][i]
    if add2 != 45:
        test.append(1)
        break

for i in range(9):
    if i%3 == 0:
        add3 = [0,0,0]
    for j in range(9):
        if j < 3:
            add3[0] += sodou[i][j]
        elif j < 6:
            add3[1] += sodou[i][j]
        else:
            add3[2] += sodou[i][j]
    if i%3 == 2:
        if add3[0]==add3[1]==add3[2]==45:
            test.append(0)
        else:
            test.append(1)
        
if 1 in test:
    print('No')
else:
    print('Yes')
        