from sys import stdin
input = stdin.readline

N = int(input())

dp = [0 for i in range(N + 1)]

if N < 3:
    print(1)
else:
    dp[1] = 1
    dp[2] = 1

    for i in range(3, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    print(dp[N])