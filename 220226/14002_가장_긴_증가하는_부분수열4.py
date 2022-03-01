N = int(input())
A = list(map(int, input().split()))
dp = [0] * N
v = [-1] * N
ans = 0
ans_arr = []
for i in range(N):
    result = []
    dp[i] = 1
    for j in range(i):
        if A[j] < A[i] and dp[j]+1 > dp[i]:
            # result.append(A[j])
            dp[i] = dp[j]+1
            v[i] = j
    # result.append(A[i])
    if ans < dp[i]:
        ans = dp[i]
        # ans_arr = result
# print("dp : ", dp)
print(ans)
val = [i for i,x in enumerate(dp) if x == ans][0]
# print("A: ", A)
# print("v: ",v)
# print("val : ", val)
while val != -1:
    ans_arr.append(A[val])
    val = v[val]
    # print("val : ", val)

print(" ".join(map(str, ans_arr[::-1])))
