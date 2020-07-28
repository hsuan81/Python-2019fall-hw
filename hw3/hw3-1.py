n1 = int(input())
n2 = int(input())
n3 = int(input())
a = 30
b = 70
c = 40

def fruitCost(number, price, discount1, discount2, discount3):
    if number >= 21:
        price = price*discount1
    elif number >= 16:
        price = price*discount2
    elif number >= 11:
        price = price*discount3
    else:
        price = price
    return price
def totalCost (number1, number2, number3, price1, price2, price3):
    if number1+number2+number3 >= 30:
        price1, price2, price3 = 0.87*price1, 0.87*price2, 0.87*price3
    total = number1*price1 + number2*price2 + number3*price3
    print('%d'%total)
        
a = fruitCost(n1, a, 0.8, 0.9, 0.95)
b = fruitCost(n2, b, 0.75, 0.85, 0.9)
c = fruitCost(n3, c, 0.8, 0.8, 0.85 )
total = totalCost(n1, n2, n3, a, b, c)
    
'''if n1 >= 21:
    a = a*0.8
elif n1 >= 16:
    a = a*0.9
elif n1 >= 11:
    a = a*0.95
else:
    a = a
    
if n2 >= 21:
    b = b*0.75
elif n2 >= 16:
    b = b*0.85
elif n2 >= 11:
    b = b*0.9
else:
    b = b
    
if n3 >= 21:
    c = c*0.8
elif n3 >= 16:
    c = c*0.8
elif n3 >= 11:
    c = c*0.85
else:
    c = c
if n1+n2+n3 >=30:
    a, b, c, = 0.87*a, 0.87*b, 0.87*c'''