from itertools import combinations

N, S = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
for i in range(1, N+1):
    C = list(combinations(arr, i))
    for c in C:
        if sum(c) == S:
            ans +=1

print(ans)