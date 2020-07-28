m = int(input())
n = int(input())

def add_with_2gap(number1, number2):
    s = 0
    for i in range(number1,number2+1,2):
        s += i
    print(s)

def product_with_3gap(number1, number2):
    d = 1
    for i in range(m,n+1,3):
        d = d*i
    print(d)

addtion = add_with_2gap(m, n)
product = product_with_3gap(m, n)