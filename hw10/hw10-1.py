n1 = input()
set1 = set(input().split(' '))
op = input()
n2 = input()
set2 = set(input().split(' '))

#注意有些運算子的結果是T or F，直接印出即可
def set_operate(set1, set2, op):
    if op == '&':
        outcome = set1 & set2
        print_order(outcome)
    elif op == '|':
        outcome = set1.union(set2)
        print_order(outcome)
    elif op == '-':
        outcome = set1.difference(set2)
        print_order(outcome)
    elif op == '^':
        outcome = set1 ^ set2
        print_order(outcome)
    elif op == '>':
        print(set1 > set2)
    elif op == '<':
        print(set1 < set2)
    elif op == '>=':
        print(set1 >= set2)
    elif op == '<=':
        print(set1 <= set2)
    elif op == '==':
        print(set1 == set2)
    
def print_order(outcome):
    out = list(sorted(outcome))   #依字母排序
  
    print('{',end='')
    for i in out:
        if out.index(i) == 0:  #空集合
            break
        else:      
            print(',', end='')
            print(' ', end = '')
            print("'%s'" %i, end='')
    print('}',end='')

set_operate(set1, set2, op)