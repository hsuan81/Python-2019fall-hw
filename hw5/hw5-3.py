def check_prime(number):
    if number <= 200:
        for i in range(2, number):
            if number % i == 0:  #有數可整除就非質數
                print('%d is not prime number' %number)
                break        
            else:
                if i == (number-1):  #迴圈終止條件
                    print('%d is prime number' %number)
                else:
                    continue

input_number = int(input())
check_result = check_prime(input_number)