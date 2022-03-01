N = int(input())
P = [0] + list(map(int, input().split()))
dp = [-1] * (N+1)
dp[0] = 0
for i in range(1, N+1):
    for j in range(1, i+1):
        if dp[i] == -1 or dp[i] > dp[i-j] + P[j]:
            dp[i] = dp[i-j]+P[j]
print(dp[N])