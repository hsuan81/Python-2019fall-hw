n = int(input())

def sectionlist(number):
    point = []
    for i in range(number):         
        x = input().split(',')
        setx = set(k for k in range(int(x[0]),int(x[1])+1)) 
        if len(point) == 0:
            point.append(setx)
        else:
            add_section(setx, point)
    
    new = point.copy()
    for i in point:
        
        if i in new:
            for j in range(len(point)):
                
                if i == point[j]:
                    continue
                elif i & point[j] and point[j] in new:
                    new[new.index(i)].update(point[j])
                    new.remove(point[j])
                
    k = []
    for j in range(len(new)):
        k.append([min(new[j]), max(new[j])])
    k.sort()
    for i in k:
        print('%d,%d' %(i[0],i[1]))

def add_section(setx, point):
    for i in point:
        if setx & i:
            ind = point.index(i)
            point[ind].update(setx)
            break
        if point.index(i) == len(point)-1:
            point.append(setx)

sectionlist(n)  