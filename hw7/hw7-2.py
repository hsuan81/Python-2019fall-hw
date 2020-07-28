r1 = input().split(' ')
def transfer_point(card):
    point = ['J', 'Q', 'K']
    if card in point:
        card = 0.5
    elif card == 'A':
        card = 1
    else:
        card = int(card)
    return card
def compare_point(round1):
    x_card = 1
    y_card = 1
    x_sum = transfer_point(round1[0])
    y_sum = transfer_point(round1[1])
    while x_card < 5 and y_card < 5:
        round = input().split(' ')
        if len(round) == 2:
            break

        elif len(round) == 3:
            if round[0] == '1':
                round[1] = transfer_point(round[1])
                x_sum += round[1]
                x_card += 1
            elif round[1] == '1':
                round[2] = transfer_point(round[2])
                y_sum += round[2]
                y_card += 1

        elif len(round) == 4:
            round[1] = transfer_point(round[1])
            x_sum += round[1]
            x_card += 1
            round[3] = transfer_point(round[3])
            y_sum += round[3]
            y_card += 1
                
        if x_sum > 21:
            x_sum = 0       
            break
        if y_sum > 21:
            y_sum = 0
            break
 
    if x_sum > y_sum :
        print('Player X is Winner')
        if type(x_sum) == float:
            print('Player X $ %.1f' % x_sum)
        else:
            print('Player X $ %d' % x_sum)
        if type(y_sum) == float:
            print('Player Y $ %.1f' % y_sum)
        elif y_sum == 0:
            print('Player Y $ Bang!')
        else:
            print('Player Y $ %d' % y_sum)
    elif y_sum > x_sum:
        print('Player Y is Winner')
        if type(x_sum) == float:
            print('Player X $ %.1f' % x_sum)
        elif x_sum == 0:
            print('Player X $ Bang!')
        else:
            print('Player X $ %d' % x_sum)
        if type(y_sum) == float:
            print('Player Y $ %.1f' % y_sum)
        else:
            print('Player Y $ %d' % y_sum)

compare_point(r1)