N = int(input())
Nums = list(map(int, input().split()))
Operator = list(map(int, input().split()))

Min = 1000000000
Max = -1000000000

def dfs(Num, idx, add, sub, mul, div):
    global Min, Max
    if idx == N:
        Min = min(Min, Num)
        Max = max(Max, Num)

    if add:
        dfs(Num + Nums[idx], idx + 1, add-1, sub, mul, div)
    if sub:
        dfs(Num - Nums[idx], idx + 1, add, sub-1, mul, div)
    if mul:
        dfs(Num * Nums[idx], idx + 1, add, sub, mul-1, div)
    if div:
        dfs(int(Num / Nums[idx]), idx + 1, add, sub, mul, div-1)

dfs(Nums[0], 1, Operator[0],Operator[1],Operator[2],Operator[3])
print(Max)
print(Min)