n1 = input()
n2 = input()
n3 = input().split(' ')
n4 = input().split(' ')
reward1 = {n1:10000000, n2:2000000, n3[0]:200000, n3[1]:200000, n3[2]:200000}
reward2 = {str(n3[0])[1:]:40000, n3[1][1:]:40000, n3[2][1:]:40000, n3[0][2:]:10000, n3[1][2:]:10000, n3[2][2:]:10000,
           n3[0][3:]:4000, n3[1][3:]:4000, n3[2][3:]:4000, n3[0][4:]:1000, n3[1][4:]:1000, n3[2][4:]:1000,n3[0][5:]:200, n3[1][5:]:200, n3[2][5:]:200,n4[0]:200, n4[1]:200, n4[2]:200}

num = int(input())
invoice = []
for i in range(num):
    x = input()
    invoice.append(x)

money = 0
for i in invoice:
    if i in reward1.keys():
        money += reward1[i]
    else:
        if i[1:] in reward2.keys():
            money += reward2[i[1:]]
        elif i[2:] in reward2.keys():
            money += reward2[i[2:]]
        elif i[3:] in reward2.keys():
            money += reward2[i[3:]]
        elif i[4:] in reward2.keys():
            money += reward2[i[4:]]
        elif i[5:] in reward2.keys():
            money += reward2[i[5:]]
        
print(money)