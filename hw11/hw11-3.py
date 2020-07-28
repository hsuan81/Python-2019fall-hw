n1 = int(input())
votes = {}
for i in range(n1):
    store_name = input()
    votes[str(i+1)] = [0, store_name]

n2 = int(input())
for i in range(n2):
    vote = input()
    votes[vote][0] += 1

result = sorted(votes.values(), reverse=True)
print(result[0][1], result[0][0])