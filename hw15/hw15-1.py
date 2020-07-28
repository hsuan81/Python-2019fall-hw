N = int(input())
M = int(input())
maze1 = []
for i in range(N):
    n = input().split()
    n = [int(x) for x in n]
    maze1.append(n)

#create a graph
graph= {}
for i in range(N):
    for j in range(M):
        graph[(i,j)] = {}
        if i+1 < N:
            graph[(i,j)][(i+1,j)] = maze1[i+1][j]
        if i-1 >-1:
            graph[(i,j)][(i-1,j)] = maze1[i-1][j]
        if j+1 < M:
            graph[(i,j)][(i,j+1)] = maze1[i][j+1]
        if j-1 > -1:
            graph[(i,j)][(i,j-1)] = maze1[i][j-1]

start = (0,0)
end = (N-1, M-1)

path = {}  #起始點到node的成本
adj_node = {}  #
queue = []

for node in graph:
    queue.append(node)  #用來判斷是否所有點都經過
    path[node] = float("inf") #node成本起始設為無窮大
    adj_node[node] = None  #與該點連接的上一個點（為成本最低的連結）

path[start] = 0
while queue:
    # find min distance which wasn't marked as current
    min_key = queue[0]
    min_val = path[min_key]
    #確定current node的cost為最小值(因為要以最小值去更新其他unvisited的點)
    for i in range(1,len(queue)):
        if path[queue[i]] < min_val:
             min_key = queue[i]
             min_val = path[min_key]
    currt = min_key
    queue.remove(currt)

    for i in graph[currt]:
        altertive = graph[currt][i] + path[currt]
        if altertive < path[i]:
            path[i] = altertive
            adj_node[i] = currt
    
print(path[end])