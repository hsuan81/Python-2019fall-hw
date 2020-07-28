import math
a = int(input())
b = int(input())
c = int(input())
if a==0 and b==0 and c==0:
    print('無限多解')
elif a==0:
    print('無解')    
elif b*b < 4*a*c:
    print('無實數解')
else:
    x1 = ((-b)+math.sqrt(b*b-4*a*c))/(2*a)
    x2 = ((-b)-math.sqrt(b*b-4*a*c))/(2*a)
    print('%.1f\n%.1f'%(x1,x2))
# warning:the order of the if condition is vital