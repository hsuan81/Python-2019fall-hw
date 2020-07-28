p1 = int(input())
p2 = int(input())
p3 = int(input())
t1 = int(input())
t2 = int(input())
phonetime = [p1, p2, p3]
texttime = [t1, t2]

def computeFee(monthfee, phonetime, texttime, phoneprice, textprice):
    fee = phonetime[0]*phoneprice[0] + phonetime[1]*phoneprice[1] + phonetime[2]*phoneprice[2] + texttime[0]*textprice[0] + texttime[1]*textprice[1]
    if fee < monthfee:
      #print(fee)
      fee = monthfee
      #print(fee)
    else:
      fee = fee
      #print(fee)
    return fee
def bestfee(feename1,feename2, feename3, fee1, fee2, fee3):#比大小的邏輯要注意
    if fee1 < fee2 and fee1 < fee3:
      print(feename1)
    else:
      if fee2 < fee3:
        print(feename2)
      else:
        print(feename3)

fee1 = computeFee(183, phonetime, texttime, [0.08,0.1393,0.1349], [1.1287,1.4803])
fee2 = computeFee(383, phonetime, texttime, [0.07,0.1304,0.1217], [1.1127,1.2458])
fee3 = computeFee(983, phonetime, texttime, [0.06,0.1087,0.1018], [0.9572,1.1243])
finalfee = bestfee('183型', '383型', '983型', fee1, fee2, fee3)