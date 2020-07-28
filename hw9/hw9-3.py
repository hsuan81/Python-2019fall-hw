def str_gcd(str1, str2):
    if str1 == str2*str1.count(str2):                 #原始字串有倍數關係
        return str2
    elif str2 not in str1 and len(str2) <= len(str1):  #原始字串並不存在另一字串中
        return 'No GCD'
    else:
        if len(str2) > len(str1):      #固定str2的長度比較短
            return str_gcd(str2, str1)
        elif str2 in str1 and len(str1)%len(str2) != 0:  #原始字串存在另一字串中，但兩者長度不具有倍數關係
            if len(str2) %2 == 0:                        #以第二字串的因數字與第一字串比較，分成len(str2)為雙數及單數的情形
                return str_gcd(str1, str2[:len(str2)//2])     
            else:
                return str_gcd(str1, str2[:1])
        else:                #第二字串的因數字存在於第一字串，但不存在倍數關係                
            return 'No GCD'

while True:
    text = input().split(' ')
    if text[0] == '-1':
        break
    else:
        print(str_gcd(text[0],text[1]))