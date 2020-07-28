A = input()
P = ' '+input()+' '
Q = ' '+input()
R = A.replace(P,Q+' ')
print(R)
I = Q+P
Id = A.replace(P,I)
print(Id)
Pd = A.replace(P,' ')
print(Pd)
#As = A.split(' ')
#S = [As[0]+Q, As[1], As[2], As[3], As[4]+Q, As[5], As[6], As[7]]
#T = ' '
#TS = T.join(S)
#print(TS)