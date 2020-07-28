article = input().split(' ')
order = list(map(int, input().split(' ')))
for_sort = []
for i in range(len(order)):
    for_sort.append([order[i], article[i]])

def orderlis(elem):
    return elem[0]

def sorted_article(for_sort):
    for_sort.sort(key = orderlis)
    _sort_ = []
    for i in for_sort:
        _sort_.append(i[1])
    print(''.join(_sort_))
        

sorted_article(for_sort)  
        