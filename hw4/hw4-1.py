m = int(input())
n = int(input())
s = 0
for i in range(m,n+1,2):
        s += i
print(s)
d = 1
for i in range(m,n+1,3):
    d = d*i
print(d)