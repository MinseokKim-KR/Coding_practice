from collections import deque
MAX = 200000
check = [False] * MAX
time = [-1] * MAX
N, M = map(int, input().split())
q = deque()
q.append(N)
check[N] = True
time[N] = 0

while q:
    s= q.popleft()
    if s-1 >=0 and check[s-1] == False:
        time[s-1] = time[s] + 1
        check[s-1] = True
        q.append(s-1)
    if s+1 < MAX and check[s+1] == False:
        time[s+1] = time[s] + 1
        check[s+1] = True
        q.append(s+1)
    if s*2 < MAX and check[s*2] == False:
        time[s*2] = time[s]
        check[s*2] = True
        q.append(s*2)
print(time[M])