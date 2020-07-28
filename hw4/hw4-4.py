def calculate_bmi(name, weight, height):
    height = height/100
    bmi = weight/height**2
    if bmi > 24:
        print('Hi %s, Your BMI: %f too HIGH.'%(name, bmi))
    elif bmi < 18.5:
        print('Hi %s, Your BMI: %f too LOW.'%(name, bmi))
    else:
        print('Hi %s, Your BMI: %f.'%(name, bmi))

name1 = input()
height1 = int(input())
weight1 = int(input())
bmi_result = calculate_bmi(name1, weight1, height1)