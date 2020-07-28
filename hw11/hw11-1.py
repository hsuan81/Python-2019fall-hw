n1 = int(input())
time_text = {}
for i in range(n1):
    text = input().split(' ', 1)
    time_text[text[0]] = text[1]

n2 = int(input())
read_time = []
for i in range(n2):
    t = int(input())  
    read_time.append(t) 

read = []
readtext = []
for i in read_time:
    for j in time_text.keys():
        #print(j)
        if int(j) <= i and j not in read:
            #print(time_text[j])
            readtext.append(time_text[j])
            read.append(j)
        elif int(j) > i :
            if readtext == [] or read_time.index(i) == len(read_time)-1:  #頭尾處理
                break
            elif readtext [-1] == '-':  #連續兩次讀取未有新增已讀訊息
                break
            else:
                readtext.append('-')
                break
for i in time_text.keys():  #看是否還有未讀訊息
    if i not in read:
        readtext.append(time_text[i])    

for k in readtext:
    print(k)