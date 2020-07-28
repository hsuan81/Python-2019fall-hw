num = input()

c = [1,1]
for i in range(2, len(num) + 1):
    if 10 < int(num[i - 2:i]) <= 26 and num[i - 1] != '0':
        c.append(c[i - 1] + c[i - 2])
    elif int(num[i - 2:i]) == 10 or int(num[i - 2:i]) == 20:
        c.append(c[i - 2])
    elif num[i-1] != '0':
        c.append(c[i - 1])

print(c[len(num)])