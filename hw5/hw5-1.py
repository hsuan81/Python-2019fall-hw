def right_triangle(number):
    for i in range(number):
        print('*', end='')  

def left_space(number):
    for j in range(number):
        print('.', end='')  

T = int(input())
N = int(input())

if T == 1:
    for k in range(N//2+1):
        right_triangle(k+1)   
        print()
    for k in range(N//2,0,-1):
        right_triangle(k)
        print()
elif T == 2:
    for k in range(N//2+1):
        left_space(N//2-k)        
        right_triangle(k+1)
        print()
    for k in range(N//2,0,-1):
        left_space(N//2-k+1)
        right_triangle(k)
        print()
elif T == 3:
    for k in range(N//2+1):
        left_space(N//2-k)        
        right_triangle(2*k+1)  
        print()
    for k in range(N//2,0,-1):
        left_space(N//2-k+1)
        right_triangle(2*k-1)
        print()

'''#first pattern
for k in range(N//2+1):    
    for i in range(k+1):
        print('*', end='')
    print()
for k in range(N//2,0,-1):
    for j in range(k):
        print('*',end='')
    print()
#second pattern
for k in range(N//2+1):
    for i in range(N//2-k):
        print(' ',end='')
    for j in range(k+1):
        print('*', end='')
    print()
for k in range(N//2,0,-1):
    for i in range(N//2-k+1):
        print(' ',end='')
    for j in range(k):
        print('*',end='')
    print()
#third pattern
for k in range(N//2+1):
    for i in range(N//2-k):
        print(' ',end='')
    for j in range(k+1):
        print('*', end='')    
    for l in range(k):    
        print('*', end='')
    print()    
for k in range(N//2,0,-1):
    for i in range(N//2-k+1):
         print(' ',end='')
    for j in range(k):
        print('*',end='')
    for l in range(k-1):
        print('*',end='')
    print()'''