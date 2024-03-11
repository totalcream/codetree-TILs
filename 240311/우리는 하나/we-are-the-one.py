from sys import stdin, setrecursionlimit
from collections import deque
from itertools import combinations
input = stdin.readline

setrecursionlimit(10**4)
N, K, U, D = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

visited = [[0] * N for _ in range(N)]

#(y, x)
directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
max_val = 0

choose = []
for i in range(N):
    for j in range(N):
        choose.append((i, j))

def in_range(y, x):
    return 0 <= x < N and 0 <= y < N

def can_go(y, x, py, px):
    if not in_range(y, x):
        return False
    if visited[y][x]:
        return False
    if abs(board[y][x]-board[py][px]) < U or abs(board[y][x]-board[py][px]) > D:
        return False
    return True

cities = list(combinations(choose, K))
def bfs():
    while dq:
        y, x = dq.popleft()
    for dy, dx in directions:
        nx = x + dx
        ny = y + dy

        if can_go(ny, nx, y, x):
            dq.append((ny, nx))
            visited[ny][nx] = 1


for city in cities:
    visited = [[0] * N for _ in range(N)]
    dq = deque()
    for c in city:
        dq.append(c)
        y, x = c
        visited[y][x] = 1
    
    bfs()
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                cnt += 1
    
    max_val = max(max_val, cnt)

print(max_val)