N = input()
new_N = N.split(' ')

def arithmetic(initial, last, difference):
    numberlis = []
    for i in range(initial, last+1, difference):
        print(i, end=' ')
        numberlis.append(i)
    print()
    return numberlis
def sum_arithmetic(numberlis):
    number_sum = 0
    for i in numberlis:
       number_sum += i
    print(number_sum)

numberlis = arithmetic(int(new_N[0]), int(new_N[1])+1, int(new_N[2]))
sum_arithmetic(numberlis)
