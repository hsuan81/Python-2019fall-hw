def even_sum(number1, number2):
    all_sum = 0
    if number1 % 2 == 0:
        number1 = number1
    else:
        number1 = number1 + 1
    if number2 % 2 == 0:
        number2 = number2
    else:
        number2 = number2 - 1
    for i in range(number1, number2+1, 2):
        all_sum += i
    return all_sum

a = int(input())
b = int(input())
print(even_sum(a,b))