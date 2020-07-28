def input_class(classalltime): 
#this funtion can use 'while' compare the len of a classlist with hours to simplify the coding  
    
    if classalltime == '3':
        x1 = input() 
        x2 = input()
        x3 = input()
        classlist = [x1, x2, x3]
    elif classalltime == '2':
        x1 = input()
        x2 = input()
        classlist = [x1, x2]
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
'''def classList(*classtime):
    classlist = list(*classtime)
    return classlist'''

def class_conflict(classname1, classname2, classlist1, classlist2):
    '''classlist1 = classlist[0]
    classlist2 = classlist[1]
    classlist3 = classlist[2]'''
    for i in classlist1:
        if i in classlist2:
            print('{0} and {1} confict on {2}'.format(classname1, classname2, i))
        
    '''for i in classlist2:
        if i in classlist3:
            print('{0} and {1} conflict on {2}'.format(classname2, classname3, i))'''

conflict12 = class_conflict(x, y, classlist1, classlist2)
conflict13 = class_conflict(x, z, classlist1, classlist3)
conflict23 = class_conflict(y, z, classlist2, classlist3)

