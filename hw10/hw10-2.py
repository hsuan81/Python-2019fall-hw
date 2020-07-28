#考試版
m = input()
s = input()

#設定字串開頭範圍（避免碰到index out of range)
r = len(m)-len(s)+1  #範圍：長字串最後可容納短字串的第一個字

p = {}
for i in range(r):
    sset = list(s)  #短字串轉為list比較
    h = i           #記下字串開頭位置
    for j in range(i,len(m)):  
        if m[j] in sset:      #找到相同字母，在短字串list做標記（刪除）
            sset.remove(m[j])

        if len(sset) == 0:    #所有短字串的文字皆找到
            p[len(m[h:j+1])] = m[h:j+1]   #存取該字串進字典key=字串長度, value=字串，並停止尋找（如果會有兩個長度相同的就無法這樣設key)
            break                         

pv = sorted(p.keys())  #依字串長度排大小
print(p[pv[0]])     