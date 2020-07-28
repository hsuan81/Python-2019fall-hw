A = input()
B = input()
x = input()
y = input()
C = A+B
D = C.replace(x, y)
print(len(C)+len(D))
Dt = D[0:3]+D[-3:]
print(Dt*3)