#考試版
n = int(input())
setn = set()

#區間讀取放入set
for i in range(n):
    sec = list(map(int,input().split(',')))
    for j in range(sec[0],sec[1]):  #因所有區間皆放入一個set，為方便判斷斷點，不放入各區間尾端的數字（讓各區間的數字間隔都增加1)
        setn.add(j)
#轉為list排序
setlis = list(setn)
setlis.sort()

print(str(setlis[0])+',', end = '')   #印出最左端
for i in range(len(setlis)):
    if i == len(setlis)-1:    #印出最尾端
        print(setlis[i]+1)
    elif setlis[i+1] - setlis[i] > 1:    #判斷非連續部分
        print(setlis[i]+1)               #加回尾端數字印出換行
        print(str(setlis[i+1])+',', end = '')   #印下一段的左端