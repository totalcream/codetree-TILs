N = int(input())

dp = [0] * (N + 1)
dphalf = [0] * (N + 1)
MOD = 1000000007

if N == 1:
    print(2)
elif N == 2:
    print(7)
else:
    dp[1] = 2
    dp[2] = 7
    dphalf[1] = 1
    dphalf[2] = 3
    for i in range(3, N + 1):
        dp[i] = ((dp[i-1]*2) + dp[i - 2] + (dphalf[i-1]*2)) % MOD
        dphalf[i] = (dp[i - 1] + dphalf[i - 1]) % MOD

    print(dp[N])