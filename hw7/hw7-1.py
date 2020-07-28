n = int(input())
def sectionlis(number):
    point = []
    for i in range(n):         
        x = input().split(' ')
        nx = list(map(int, x))  #將list內各個元素變成int，map(function, iterables)回傳各個序列元素透過func的結果
        point.append(nx)

    for i in point:          
        index = point.index(i)
        for j in point[index+1:n+1]:             #利用index取出list內的元素的範圍，用於向後面的元素比較
            if i[0] == i[1]:
                continue
            elif i[0] >= j[0] and i[1] <= j[1]:  #線段a在線段b的範圍內
                i[0] = i[1]
            elif i[0] < j[0] and i[1] > j[1]:    #線段a比線段b長，但兩者有重合
                j[0] = j[1]
            elif i[0] >= j[0] and i[0] <= j[1]:  #線段a起點在線段b的範圍內
                i[0] = j[1]
            elif i[1] >= j[0] and i[1] <= j[1]:  #線段a終點在線段b的範圍內
                i[1] = j[0]
    return point

def section_length(section_list):
    sum_line = 0
    for i in section_list:
        sum_line += i[1] - i[0]
    print(sum_line)

section = sectionlis(n)
section_length(section)