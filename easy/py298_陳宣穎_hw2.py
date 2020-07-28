n = int(input('Please input a number:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,'*',j,'=',i*j)
    

m = int(input('Please input a number:'))
while m>1:
    for x in range(1,m+1):
        for y in range(1,m+1):
            print(x,'*',y,'=',x*y)
    if x==y==m:
        break
