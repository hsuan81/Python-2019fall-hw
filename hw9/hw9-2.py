def gcd_3(n1,n2,n3):
    if n2 == 0 and n3 == 0:
        return n1
    else:
        if n1 == 0:                  #固定做輾轉相除的順序後，處理當除數為0時，直接換位子繼續下一輪相除
            return gcd_3(n2, n3, n1)
        else:    
            return gcd_3(n2%n1, n3%n1, n1)

while True:
    n = input().split(' ')
    n = list(map(int, n))
    if n[0] == -1:
        break
    else:
        print(gcd_3(n[0],n[1],n[2]))