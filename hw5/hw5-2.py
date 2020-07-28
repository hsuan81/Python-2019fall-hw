N = int(input())
def print_line(number):
    for k in range(number):      #k loop 決定要印幾行，以及各行的符號變化
        print_hashtag(number+k)  #loop 參數值考慮跟k loop的關係
        print_number(number-k)   #loop 參數值考慮跟k loop的關係
        print()
def print_hashtag(number):        
    for i in range(number):
            print('#', end='')
def print_number(number):            
    for j in range(number, 0,-1):
        print(j,end='')

print_line(N)