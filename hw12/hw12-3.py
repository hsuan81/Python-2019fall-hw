#如果迴圈的這個為數字，同時檢查下一個是不是數字，不是的話就多插一個間隔符號
#再reverse

text = input()

def get_password(text):
    numberlis = []
    end = len(text)-1
    for i in range(len(text)):
        if text[i].isdigit():
            numberlis.append(text[i])
            if i == end:                   #字尾調整
                break
            elif not text[i+1].isdigit():  #下一個位子非數字再加分隔符號
                numberlis.append('+')

    rev_numberlis = numberlis[::-1]        #反轉順序
    rev_number = ''.join(rev_numberlis)    #以空字元合併
    rev = rev_number.split('+')            #用原本的分隔符號切數字

    sum = 0   
    for i in rev:
        if i != '':              #切片時可能產生空字元
            sum += int(i)
    print(sum)

get_password(text)    
