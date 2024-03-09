from sys import stdin, setrecursionlimit
import copy

input = stdin.readline
setrecursionlimit(10**9)

N, M = map(int, input().split())

board = []
directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]

max_val = 0
for i in range(N):
    board.append(list(map(int, input().split())))
    max_val = max(max_val, max(board[i]))

zone = []
for i in range(max_val):
    new_board = copy.deepcopy(board)
    for j in range(N):
        for k in range(M):
            new_board[j][k] -= i + 1
    zone.append(new_board)
    
def dfs(k, y, x):
    zone[k][y][x] = 0

    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < M and 0 <= ny < N and zone[k][ny][nx] > 0:
            dfs(k, ny, nx)

ans = []
for i in range(max_val):
    cnt = 0
    for j in range(N):
        for k in range(M):
            if zone[i][j][k] > 0:
                dfs(i, j, k)
                cnt += 1
    #print(zone[i])
    ans.append(cnt)

max_safezone_cnt = max(ans)
max_safezone_index = ans.index(max_safezone_cnt)
print(f"{max_safezone_index + 1} {max_safezone_cnt}")