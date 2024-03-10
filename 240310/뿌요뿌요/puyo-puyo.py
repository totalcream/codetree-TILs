# import sys
# import os

# for i in range(int(sys.stdin.readline())):
#     #입력
#     a,K = map(int,sys.stdin.readline().split())
#     c = sorted(map(int,sys.stdin.readline().split()))
#     #d: 정답 저장 리스트
#     d = []
#     gz = min(c)
#     pz = max(c)
#     for l in range(len(c)):
#         #만약 l과 가장 작은 수를 더해도 K에 가장 작은 d를 더한경우보다 크거나, l과 가장 큰 수를 더해도 b에 가장 작은 d를 뺀 경우와 같을 경우 탐색 건너뜀.
#         if len(d) != 0:
#             if l + gz < K + d[0] or l + pz + d[0] > K:
#                 pass
#             else:
#                 continue
#         #같은 수끼리 더하지 않게 함
#         e = c[:]
#         e.remove(c[l])
#         #이분탐색, 각 수에 대해 합이 가장 가까운 두 수를 찾음
#         mn = 0
#         mx = len(e)-1
#         while mn+1 != mx:
#             mid = (mn+mx)//2
#             if c[l]+e[mid] == K:
#                mx = mid
#                mn = mid
#                break
#             elif c[l] +e[mid] > K:
#                mx = mid
#             elif c[l] + e[mid] < K:
#                 mn = mid
#         #이분탐색으로 나온 가장 가까운 두 수에 대해 계산       
#         dea = abs(c[l]+e[mn]-K)
#         deb = abs(c[l]+e[mx]-K)
#         de = min(dea,deb)
#         #정답 저장하는 수열의 첫번째 값과 과 비교
#         if len(d) == 0 or d[0] > de:
#             #정답 수열의 첫번째 값보다 작다면 정답 수열을 초기화하고 값을 추가.
#             d = [de]
#             if dea == deb:
#                 if mn != mx:
#                     #만약 이분탐색으로 나온 두 수가 같다면 두번 추가
#                     d.append(de)
#             #만약 정답수열의 첫번째 값과 같다면 정답 수열에 추가.
#         elif d[0] == de:
#             if dea == deb:
#                 if mn != mx:
#                     #만약 이분탐색으로 나온 두 수가 같다면 두번 추가
#                     d.append(de)
#             d.append(de)
#     #d의 길이 //2 를 출력.
#     sys.stdout.write(str(len(d)//2)+'\n')

# n, m, v = map(int, input().split())
# graph = [[]] * (n+1)
# visited = [False] * (n+1)

# for _ in range(m):
#   f, t = map(int, input().split())
#   if graph[f] == []:
#     graph[f] = [t]
#   else:
#     graph[f].append(t)
#   if graph[t] == []:
#     graph[t] = [f]
#   else:
#     graph[t].append(f)

# from collections import deque

# def bfs(graph, i, visited):
#   queue= deque()
#   queue.append(i)
#   while queue:
#     value = queue.popleft()

#     if not visited[value]:
#       print(value, end=' ')
#       visited[value] = True
#       for j in graph[value]:
#         queue.append(j)

# bfs(graph, v, visited)

# n, m, v = map(int, input().split())
# matrix = [[0] * (n+1) for _ in range(n+1)]
# visited = [False] * (n+1)

# for _ in range(m):
#   f, t = map(int, input().split())
#   matrix[f][t] = matrix[t][f] = 1
  
# from collections import deque

# def bfs(matrix, i, visited):
#   queue= deque()
#   queue.append(i)
#   while queue:
#     value = queue.popleft()
#     if not visited[value]:
#       print(value, end=' ')
#       visited[value] = True
#       for c in range(len(matrix[value])):
#         if matrix[value][c] == 1 and not visited[c]:
#           queue.append(c)

# bfs(matrix, v, visited)

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
for i in range(N):
    for j in range(N):
        if board[i][j]:
            cnt = 0
            val = board[i][j]
            dfs(val, i, j)
            if cnt > 3:
                ans.append([cnt, val])
            else:
                ans.append([cnt, 0])

ans.sort()
print(f"{ans[-1][1]} {ans[-1][0]}")