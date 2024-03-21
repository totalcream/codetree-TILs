from sys import stdin
input = stdin.readline

N = int(input())

dp = [0] * (N + 1)
MOD = 10007

if N < 3:
    print(1)
else:
    dp[2] = 1
    dp[3] = 1
    for i in range(4, N + 1):
        if i >= 2:
            dp[i] = ((dp[i] + dp[i - 2]) % MOD)
        if i >= 3:
            dp[i] = ((dp[i] + dp[i - 3]) % MOD)
    
    print(dp[N])