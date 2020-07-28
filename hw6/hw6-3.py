def find_factor(number):
    factorlis = []
    for i in range(2, number):
        while number % i == 0:
            factorlis.append(i)
            number = number//i
            if number == 1:
                break
    
    print('*'.join(str(x) for x in factorlis))

number = int(input())
factor = find_factor(number)