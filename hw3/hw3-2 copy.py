x1 = input()
x2 = input()
x3 = input()
y1 = input()
y2 = input()
y3 = input()
'''x = [x1, x2, x3]
y = [y1, y2, y3]'''
def computePoint(card1, card2, card3):
    cardlist = [card1, card2, card3]
    '''while card:
        cardlist.append(card)'''
    point = {'A':1, 'J':0.5, 'Q':0.5, 'K':0.5}
    for i in cardlist:
        if i in point:
            cardlist[cardlist.index(i)] = point[i]
    else:
        i = i
    totalpoint = float(cardlist[0])+float(cardlist[1])+float(cardlist[2])
    return totalpoint

def compete(totalpoint1, totalpoint2):
    '''totalpoint1 = float(cardlist1[0])+float(cardlist1[1])+float(cardlist1[2])
    totalpoint2 = float(cardlist2[0])+float(cardlist2[1])+float(cardlist2[2])'''
    print('%d\n%d'%(totalpoint1, totalpoint2))
    if totalpoint1 > 10.5 and totalpoint2 > 10.5:
        print('平手')
    elif totalpoint2 > 10.5:
        print('A贏')
    elif totalpoint1 > 10.5:
        print('B贏')
    elif totalpoint1 > totalpoint2:
        print('A贏')
    elif totalpoint2 > totalpoint1:
        print('B贏')
    else:
        print('平手')
A = computePoint(x1, x2, x3)
B = computePoint(y1, y2, y3)
result = compete(A,B)

'''point = {'A':1, 'J':0.5, 'Q':0.5, 'K':0.5} #這種寫法後面要記得將文字轉成數字型態，另一種同樣效果可以用兩個list搭配for寫
for i in x:
    if i in point:
        x[x.index(i)] = point[i]
    else:
        i = i
for i in y:
    if i in point:
        y[y.index(i)] = point[i]
    else:
        i = i'''
#這種寫法還是不對，因為如果一個人同時拿到兩張同樣的文字牌第二張不會轉換成數字，除非再寫一個and的可能，但那樣子程式會太長
'''if x1 or x2 or x3 == 'A':
    if x1 == 'A':
        x1 = 1 
    elif x2 == 'A':
        x2 = 1
    else:
        x3 = 1
if y1 or y2 or y3 == 'A':
    if y1 == 'A':
        y1 = 1
    elif y2 == 'A':
        y2 = 1
    else:
        y3 = 1
if x1 or x2 or x3 == 'J':
    if x1 == 'J':
        x1 = 0.5 
    elif x2 == 'J':
        x2 = 0.5
    else:
        x3 = 0.5
if y1 or y2 or y3 == 'J':
    if y1 == 'J':
        y1 = 0.5
    elif y2 == 'J':
        y2 = 0.5
    else:
        y3 = 0.5
if x1 or x2 or x3 == 'Q':
    if x1 == 'Q':
        x1 = 0.5 
    elif x2 == 'Q':
        x2 = 0.5
    else:
        x3 = 0.5
if y1 or y2 or y3 == 'Q':
    if y1 == 'Q':
        y1 = 0.5
    elif y2 == 'Q':
        y2 = 0.5
    else:
        y3 = 0.5
if x1 or x2 or x3 == 'K':
    if x1 == 'K':
        x1 = 0.5 
    elif x2 == 'K':
        x2 = 0.5
    else:
        x3 = 0.5
if y1 or y2 or y3 == 'K':   
    if y1 == 'K':
        y1 = 0.5
    elif y2 == 'K':
        y2 = 0.5
    else:
        y3 = 0.5
print(x1,x2,x3)
print(y1,y2,y3)'''
        
'''X = float(x[0])+float(x[1])+float(x[2])
Y = float(y[0])+float(y[1])+float(y[2])
print('%d\n%d'%(X,Y))
if X > 10.5 and Y < 10.5:
    print('B贏')
elif Y > 10.5 and X< 10.5:
    print('A贏')
elif 10.5 > X and X > Y:
    print('A贏')
elif 10.5 > Y and Y > X:
    print('B贏')
else:
    print('平手')'''