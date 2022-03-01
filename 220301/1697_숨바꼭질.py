from collections import deque

MAX = 200000
check = [False] * (MAX+1)
dist = [-1] * (MAX+1)
N, M = map(int, input().split())
check[N] = True
dist[N] = 0
q = deque()
q.append(N)
while q:
    now = q.popleft()
    for next in [now-1, now+1, now*2]:
        if 0 <= next <= MAX and check[next] == False:
            check[next] = True
            dist[next] = dist[now] +1
            q.append(next)

print(dist[M])