from itertools import permutations 
text = input().split(' ')

def no_repetitionmin(text):
    text = list(permutations(text))
    text.sort()
    text = list(''.join(i) for i in text)

    for i in text:
        minnum = text[0]
        for j in minnum:
            if j+j in minnum:
                text.remove(minnum)
                break
    print(text[0])

no_repetitionmin(text)   