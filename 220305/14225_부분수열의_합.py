from itertools import combinations

N = int(input())
arr = list(map(int, input().split()))
ans = [1] * (sum(arr)+1)
ans[0] = 0
for i in range(1, N+1):
    C = list(combinations(arr, i))
    for c in C:
        ans[sum(c)] = 0

if sum(ans) == 0:
    print(sum(arr)+1)
else:
    for idx, num in enumerate(ans):
        if num == 1:
            print(idx)
            break
