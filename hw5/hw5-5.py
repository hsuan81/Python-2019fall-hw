def factorial(number):
    if number == 1:
        return 1
    elif number > 0 and number < 16:
        result = number * factorial(number-1)
        return result
   
get_number = int(input())
print(factorial(get_number))