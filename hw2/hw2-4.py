A = input().split(' ')
D = input().split('/')
F = '{FirstName} is born at year {yyyy} month {mm} day {dd} in {LastName} family.'.format(FirstName = A[0], yyyy = D[0], mm = D[1], dd = D[2], LastName = A[1])
#warning:positional arguement shouldn't follow the keyword arguement. 
# ex: str.format(FirstName = kobe, yyyy = 1980, 12)->error
# correct: str.format(kobe, yyyy = 1980, month = 12)
print(F)