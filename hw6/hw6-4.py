def common_multiple(number1, number2):
    gcd = number1 * number2
    while number1 > 0 and number2 > 0:
        temp = number2                #用temp存number2，避免後續計算跟賦值受影響
        number2 = number1 % number2
        number1 = temp

    if number1 > 0 :
        gcd = gcd//number1
    else:
        gcd = gcd//number2
    print(gcd)

n1 = int(input())
n2 = int(input())
common_multiple(n1, n2)
