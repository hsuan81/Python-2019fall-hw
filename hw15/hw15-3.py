N = int(input())
M = int(input())
maze3 = []
for i in range(N):
    n = input().split()
    n = [int(x) for x in n]
    maze3.append(n)
#標示出口(可改在存迷宮時檢查)
for i in range(N):
    if maze3[i][M-1] == 0:
        end = [i,M-1]

best_step = N*M
step = 1
def min_mazestep(x,y,step,best_step):
    if [x,y] == end:
        if step < best_step:
            best_step = step-1 #第一步設為2以區別牆壁
            return best_step
    
    #判斷目前位置是否合法(含未到終點前已走步數同best step)
    if x > N-1 or y > M-1 or step == best_step or maze3[x][y] != 0:
        return best_step
    
    step += 1
    maze3[x][y] = step  #該點是走到第幾步

    #儲存回傳的best step值
    #(若未儲存，程式會直接call global best_step=100造成best step未記錄，若原本就會對回傳值操作ex:step，則不需要另外儲存該回傳值)
    best_step = min_mazestep(x,y+1,step,best_step)  
    best_step = min_mazestep(x+1,y,step,best_step)
    best_step = min_mazestep(x,y-1,step,best_step)
    best_step = min_mazestep(x-1,y,step,best_step)
    
    step -= 1        #已走過退回
    maze3[x][y] = 0  #不能走，或是已計算完復原算別條路
    return best_step   #不論何種操作，每次都回傳best_step，沒回傳上面儲存的best_step會為None
    

print(min_mazestep(0,1,step,best_step))