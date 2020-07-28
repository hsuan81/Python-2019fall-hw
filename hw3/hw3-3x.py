def input_class(classalltime):
    if classalltime == '3':
        x1 = input() 
        x2 = input()
        x3 = input()
        classlist = [x1, x2, x3]
    elif classalltime == '2':
        x1 = input()
        x2 = input()
        classlist = [x1, x2]
    #elif classalltime is '1':
    else:
        x1 = input()
        classlist = [x1]
    return classlist

x = input()
xt = input()
classlist1 = input_class(xt)
y = input()
yt = input()
classlist2 = input_class(yt)
z = input()
zt = input()
classlist3 = input_class(zt)

def class_conflict(classname1, classname2, classlist1, classlist2):
    c = []
    for i in classlist1:
        t = int(i)
        if t in range(11,20) and range(21,30) and range(31,40) and range(41,50) and range(51,60):
            if i in classlist2:
                c.append(i)
    if c != []:
        c = ' '.join(c)
        print('{0} and {1} conflict on {2}'.format(classname1, classname2, c))
conflict12 = class_conflict(x, y, classlist1, classlist2)
conflict13 = class_conflict(x, z, classlist1, classlist3)
conflict23 = class_conflict(y, z, classlist2, classlist3)
