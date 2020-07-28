number_of_integer = int(input())

def input_integer(number):
    integerlis = []
    while len(integerlis) < number:
        integerlis.append(int(input()))
    return integerlis
#print(integerlis)

#從大排到小
def sort_number(integer_list):
    for i in integer_list[1:]:
        index = integer_list.index(i) 
        j = integer_list[index-1]
        while i > j and index-1 >= 0:
            #print(integer_list)
            integer_list[index-1] = i
            integer_list[index] = j
            index -= 1                  # 因為i>j，所以往前移一格，index也減少一個
            #print(integer_list)
            if index >=1 :
                j = integer_list[index-1]
    return integer_list

number_list = input_integer(number_of_integer)    
sorted_list = sort_number(number_list)
#print(sorted_list)
print(sorted_list[1])
big_multiply_small = sorted_list[0] * sorted_list[-1]
print(big_multiply_small)