n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
minv = 10**10
for i in range(n):
    tmp = 0
    for j in reversed(range(n)):
        tmp += A[j] * abs(j - i)
        # print(tmp)
    if minv >= tmp:
        minv = tmp

print(minv)
        