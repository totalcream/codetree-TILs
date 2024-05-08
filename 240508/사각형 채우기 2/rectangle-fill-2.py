# 2*n 타일링 2
# 2024-05-08
# 예전에 코드트리에서 풀었던 것
# 사실 아님 사각형 채우기 2번임

N = int(input())

dp = [0] * (N + 1)
MOD = 10007
if N == 1:
    print(1)
elif N == 2:
    print(3)
elif N == 3:
    print(5)
else:
    dp[1] = 1
    dp[2] = 3
    dp[3] = 5
    for i in range(4, N + 1):
        dp[i] = (dp[i - 1] + 2*dp[i - 2]) % MOD

    print(dp[N])