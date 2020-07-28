def BMI(height, weight):
    if height > 2.5 or height < 0.5:
        print('Input Error 0.5~2.50')
    elif weight > 300 or weight < 20:
        print('Input Error 20~300')
    else:
        bmi = weight/height**2
        if bmi > 24:
            print('BMI too hight')
        elif bmi < 18.5:
            print('BMI too low')
        else:
            print('%.2f'%bmi)
    

while True:
    number = input()
    if number == '-1':
        break
    else:
        numberlis = number.split(' ')
        height = float(numberlis[0])
        weight = int(numberlis[1])
        BMI(height, weight)