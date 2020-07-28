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
    if totalpoint > 10.5:
        totalpoint = 0
    else:
        totalpoint = totalpoint
    return totalpoint

def compete(totalpoint1, totalpoint2):
    '''totalpoint1 = float(cardlist1[0])+float(cardlist1[1])+float(cardlist1[2])
    totalpoint2 = float(cardlist2[0])+float(cardlist2[1])+float(cardlist2[2])'''
    print('%d\n%d'%(totalpoint1, totalpoint2))
    if  totalpoint1 > totalpoint2:
        print('A贏')
    elif totalpoint2 > totalpoint1:
        print('B贏')
    else:
        print('平手')
A = computePoint(x1, x2, x3)
B = computePoint(y1, y2, y3)
result = compete(A,B)
