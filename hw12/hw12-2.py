num = int(input())
text = []
for i in range(num):
    x = input()
    text.append([x,0])
find = input()

#取list中item的第二個元素
def take_second(ele):
    return ele[1]

def capital_word(text,find):
    low_find = find.lower().split(' ')
    #計算相同次數及替換相同字為大寫
    for j in text:  #檢查幾個句子
        for i in low_find:  
            lowt = j[0].lower()          #檢查的句字全轉成小寫
            if lowt.count(i) > 0:        #計算次數
                j[1] += lowt.count(i)
                index = lowt.find(i)
                for k in range(lowt.count(i)):          #以index找尋取代的位置替換為大寫
                    j[0] = j[0][:index]+i.upper()+j[0][index+len(i):]
                    index = lowt.find(i, index+1)       #調整index,找下個的位置
                    
    #先做字典排序，再依次數排序（python同值以原本順序排序->排序穩定性）
    text.sort()
    text.sort(key=take_second, reverse=True)

    for i in text:
        print(i[0])

capital_word(text, find)