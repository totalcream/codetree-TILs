from sys import stdin, setrecursionlimit
from collections import deque
from itertools import combinations
input = stdin.readline

N, K, U, D = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

visited = [[False for _ in range(N)] for _ in range(N)]

#(y, x)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
max_val = 0

choose = []
for i in range(N):
    for j in range(N):
        choose.append((i, j))

cities = list(combinations(choose, K))

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

def can_go(x, y, px, py):
    if not in_range(x, y):
        return False
    if visited[x][y]:
        return False
    if abs(board[x][y]-board[px][py]) < U or abs(board[x][y]-board[px][py]) > D:
        return False

    return True

def bfs():
    while dq:
        x, y = dq.popleft()
        
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if can_go(nx, ny, x, y):
                dq.append((nx, ny))
                visited[nx][ny] = True


for city in cities:
    visited = [[False for _ in range(N)] for _ in range(N)]
    dq = deque()
    for c in city:
        dq.append(c)
        x, y = c
        visited[x][y] = True
    
    bfs()
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                cnt += 1
    
    max_val = max(max_val, cnt)

print(max_val)