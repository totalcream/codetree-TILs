from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(1000000)
N = int(input())

board = []

for i in range(N):
    board.append(list(map(int, input().split())))

#visited = [[0 for _ in range(N)] for _ in range(N)]
#(y, x) , R - D - L - U
dir = [(0, 1), (-1, 0), (0, -1), (1, 0)]

cnt = 0
ans = []
def dfs(x, y):
    global cnt
    board[y][x] = 0
    cnt += 1

    for dx, dy in dir:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < N and 0 <= ny < N and board[ny][nx]:
            dfs(nx, ny)
    return cnt

for y in range(N):
    for x in range(N):
        if board[y][x]:
            cnt = 0
            ans.append(dfs(x, y))

print(len(ans))
for a in sorted(ans):
    print(a)