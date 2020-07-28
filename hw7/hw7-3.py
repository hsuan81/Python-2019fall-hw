numberlis = input().split(' ')
numberlis = list(map(int, numberlis))

def find_number(numberlis):
    n = numberlis[0] + numberlis[1]
    while True:
        if n%numberlis[2] == numberlis[3] and n%numberlis[4] == numberlis[5]:
            break
        n += numberlis[0]
    print(n)

find_number(numberlis)