from sys import stdin, setrecursionlimit
input = stdin.readline

N = int(input())
setrecursionlimit(10**9)

board = []

for i in range(N):
    board.append(list(map(int, input().split())))

cnt = 0
val = 0
#(y, x)
directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
def dfs(val, y, x):
    global cnt
    cnt += 1
    board[y][x] = 0

    for dy, dx in directions:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < N and 0 <= ny < N and board[ny][nx] == val:
            dfs(val, ny, nx)
    return cnt

ans = []
booms = 0
for i in range(N):
    for j in range(N):
        if board[i][j]:
            cnt = 0
            val = board[i][j]
            dfs(val, i, j)
            if cnt > 3:
                ans.append(cnt)
                booms += 1
            else:
                ans.append(cnt)
ans.sort()
print(f"{booms} {ans[-1]}")