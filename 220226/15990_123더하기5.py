T = int(input())
mod = 1000000009
dp = [[0] * 4 for _ in range(100001)]
for i in range(1, 100001):
    if i-1 >=0:
        dp[i][1] = dp[i-1][2] + dp[i-1][3]
        if i == 1:
            dp[i][1] = 1
    if i-2 >= 0:
        dp[i][2] = dp[i-2][1] + dp[i-2][3]
        if i == 2:
            dp[i][2] = 1
    if i-3 >= 0:
        dp[i][3] = dp[i-3][1] + dp[i-3][2]
        if i == 3:
            dp[i][3] = 1
    dp[i][1] %= mod
    dp[i][2] %= mod
    dp[i][3] %= mod
for _ in range(T):
    N = int(input())
    print(sum(dp[N]) % mod)
