card = input().split()
color = {'S':0, 'H':0, 'D':0, 'C':0}
numberdict = {'J':11, 'Q':12, 'K':13, 'A':14}
number = [0]*13

for i in card:
    c = i[-1]
    if i[0] in numberdict.keys():
        n = numberdict[i[0]]
    else:
        n = int(i[0:len(i)-1])
    color[c] += 1
    number[n-2] += 1

if number.count(1) == 5:
    index = number.index(1) 
    index0 = number.index(0)
    if number[index:index+6].count(1) == 5:
        if 5 in color.values():
            print(8)
        else:
            print(4)
    elif number[index0:index0+9].count(0) == 8:
        if 5 in color.values():
            print(8)
        else:
            print(4)
    else:
        if 5 in color.values():
            print(5)
        else:
            print(0)

elif 4 in number:
    print(7)
elif 3 in number and 2 in number:
    print(6)
elif 5 in color.values():
    print(5)
elif 3 in number:
    print(3)
elif number.count(2) == 2:
    print(2)
elif number.count(2) == 1:
    print(1)
else:
    print(0)