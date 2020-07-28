number = list(map(int, input().split(' ')))
odd = []
even = []
for i in number:
    if i%2== 0:
        even.append(i)
    else:
        odd.append(i)

def insertion_sort(numberlis):  #小排到大
    for j in numberlis[1:]:
        index = numberlis.index(j)
        min = numberlis[index-1]
        while j < min and index-1>= 0:
            numberlis[index-1] = j 
            numberlis[index] = min
            index -= 1
            if index >= 1:
                min = numberlis[index-1]
    return numberlis

new_even = insertion_sort(even)
new_even.sort(reverse=True)
new_odd = insertion_sort(odd)
new_numberlis = new_odd + new_even
print(new_numberlis)