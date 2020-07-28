
w1 = input()
w2 = input()

def levenshtein(w1, w2):
    size_w1 = len(w1)+1
    size_w2 = len(w2)+1
    matrix = [[0]*size_w2 for i in range(size_w1)]
    for i in range(size_w1):
        matrix[i][0] = i
    for j in range(size_w2):
        matrix[0][j] = j
    for i in range(1,size_w2):
        for j in range(1,size_w1):
            l = matrix[j][i-1]+1
            r = matrix[j-1][i]+1
            if w1[j-1] == w2[i-1]:
                t = matrix[j-1][i-1]
            else:
                t = matrix[j-1][i-1]+1
            
            matrix[j][i] = min(l,t,r)
    
    return int(matrix[len(w1)][len(w2)])

print(levenshtein(w1,w2))
