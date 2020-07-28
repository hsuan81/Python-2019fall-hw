n1 =int(input())
dict1 = {}
timelist1 = []
for i in range(n1):    #讀取對話時間與內容
    time, conv = input().split(' ', 1)
    dict1[time] = conv
timelist1 = dict1.keys()    #conversation record

n2 = int(input())
timelist2 = []
for i in range(n2):    #讀取時間戳記
    time2 = int(input())
    timelist2.append(time2)    #timestamp

for t2 in timelist2:    #依時間戳記小至大依序
    count = 0    #計算此區間顯示紀錄數量
    for t1 in timelist1:
        if int(t1) <= t2 and dict1[t1] != "x":    #對話紀錄時間<= t2(時間戳記) 且未顯示過 (不為"x")
            print(dict1[t1])
            dict1[t1] = "x"    #輸出過紀錄改為"x"讓後面不再顯示
            count += 1    #計算輸出幾個
    if count != 0 and timelist2[-1] != t2:    #有輸出過且不為最後一個
        print("-")

for t1 in timelist1:    #看是否最後仍有未輸出處理
    if dict1[t1] != "x":
        print(dict1[t1])