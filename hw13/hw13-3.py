s = input()

psw = []
text= []
for i in s:
    if i.isalnum():
        if i.isalpha() and i not in text:
            t = s.count(i)
            if t < 10:
                psw.append(t)
                text.append(i)
        if i.isdigit():
             psw.append(int(i))
             text.append(i)

for k in psw:
    print(k, end='')