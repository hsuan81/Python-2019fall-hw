text = input()

def find_lowercase(string):
    lowercase = []
    for i in string:
        if i.islower():
            lowercase.append(i)
    if lowercase == []:
        print('No lowercase letters')
    else:
        lower_letter = ''.join(lowercase)
        print(lower_letter)

lowercase_text = find_lowercase(text)

length = len(text)
print(length)

def find_uppercase(string):
    number_of_uppercase = 0
    for i in string:
        if i.isupper():
            number_of_uppercase += 1
    print(number_of_uppercase)     

uppercase_number = find_uppercase(text)

