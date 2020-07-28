A = input()
P = input()
Q = input()
R = A.split(' ')
for r in R:
    if r == P:
        R[R.index(r)] = Q
print(' '.join(R))
T = A.split(' ')
for t in T:
    if t == P:
        T[T.index(t)] = Q+' '+P
print(' '.join(T))
S = A.split(' ')
for s in S:
    #print(s)
    if s == P:
        S.remove(s)
        #print(s)   
        #S[S.index(s)] = ''
print(' '.join(S))
#R = A.replace(P,Q+' ')
#print(R)
#I = Q+P
#Id = A.replace(P,I)
#print(Id)
#Pd = A.replace(P,' ')
#print(Pd)