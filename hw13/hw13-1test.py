w1 = input()
w2 = input()

def count_step(w1,w2):
    count = 0
    order = []
    #判斷長度
    if len(w1) >= len(w2):
        l = w1
        s = w2
    else:
        l = w2
        s = w1
    
    #計算增刪前的替換次數
    for i in range(len(s)):
        t = s[i]
        if t in l:  
            ind = l.index(t)
            if len(order) > 0 and ind < order[-1]:  #字母順序非遞增，要替換
                count += 1
            
            order.append(ind)
           
        else:             #字母不存在，替換
            count += 1
    #頭尾調整
    if order[1] == 0:
        if order[2] - order[0] == 1:
            count += 1
        elif order[2] - order[0] < 0:
            count += 1
    if order[-2] == len(l)-1:
        count += 1
    
    #計算刪除或插入次數
    count += len(l) - len(s)
    print(count)

count_step(w1,w2)