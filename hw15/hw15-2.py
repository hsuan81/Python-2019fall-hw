N = int(input())
M = int(input())
maze2 = []
for i in range(N):
    n = input().split()
    n = [int(x) for x in n]
    maze2.append(n)

start = [0,1]

for i in range(N):
    if maze2[i][M-1] == 0:
        end = [i,M-1]
step = []

def solve_maze(maze2,x,y,step):
    if [x,y] == end:
        maze2[x][y] = 2
        return step
    if y < M-1 and maze2[x][y+1] == 0: 
        maze2[x][y] = 2
        solve_maze(maze2,x,y+1,step)
        if maze2[x][y+1] == 2:
            step.append('r')
            return step
    if x < N-1 and maze2[x+1][y] == 0:
        maze2[x][y] = 2
        solve_maze(maze2,x+1,y,step)
        if maze2[x+1][y] == 2:
            step.append('d')
            return step
    if y > 0 and maze2[x][y-1] == 0:
        maze2[x][y] = 2
        solve_maze(maze2,x,y-1,step)
        if maze2[x][y-1] == 2:
            step.append('l')
            return step
    if x > 0 and maze2[x-1][y] == 0:
        maze2[x][y] = 2
        solve_maze(maze2,x-1,y,step)
        if maze2[x-1][y] == 2:
            step.append('u')
            return step
    if maze2[x][y] != 1:  #無法再走
        maze2[x][y] = 1

route = solve_maze(maze2,start[0],start[1],step)
route = route[::-1]
for i in route:
    print(i,end='')