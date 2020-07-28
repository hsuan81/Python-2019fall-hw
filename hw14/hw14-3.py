#除以新進制，餘數為個位，之後一直除到最後商為1或無法除盡時決定最大位數，無法除盡表示要後一位有數字，餘數為該位數的數字

num = int(input())
base = int(input())

def convert_base(num, base):
    output = []
    overdigit = {10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f', 16:'g', 17:'h', 18:'i', 19:'j', 20:'k', 21:'l', 22:'m',
                 23:'n', 24:'o', 25:'p', 26:'q', 27:'r', 28:'s', 29:'t', 30:'u', 31:'v', 32:'w', 33:'x', 34:'y', 35:'z'}

    while num >= base:
        remainder = num % base
        num = num//base

        #餘數超過9要轉換
        if remainder > 9:
            remainder = overdigit[remainder]
        output.append(remainder)

    #最後的商數超過9轉換
    if num > 9:
        num = overdigit[num]
    output.append(num)

    #轉換位數方向從大位數到小位數
    output = output[::-1]
    
    for i in output:
        print(i, end='')

convert_base(num, base)