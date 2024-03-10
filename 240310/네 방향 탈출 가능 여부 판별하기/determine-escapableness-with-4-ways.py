from sys import stdin, setrecursionlimit
from collections import deque
input = stdin.readline

setrecursionlimit(10**4)
N, M = map(int, input().split())

board = []
for i in range(N):
    board.append(list(map(int, input().split())))

visited = [[0] * M for _ in range(N)]

#(y, x)
directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
dq = deque()
def bfs():
    visited[0][0] = True
    while dq:
        y, x = dq.popleft()
        for dy, dx in directions:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < M and 0 <= ny < N:
                if not visited[ny][nx] and board[ny][nx]:
                    visited[ny][nx] = 1
                    dq.append((ny, nx))


dq.append((0, 0))
bfs()
print(visited[N-1][M-1])