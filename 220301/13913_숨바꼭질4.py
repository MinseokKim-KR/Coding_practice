from collections import deque
import sys
MAX = 2000000
sys.setrecursionlimit(MAX)
check = [False] * MAX
dist = [-1] * MAX
visit = [-1] * MAX
N, M = map(int, input().split())
check[N] = True
dist[N] = 0

q = deque()
q.append(N)

while q:
    now = q.popleft()
    if now -1 >= 0 and not check[now-1]:
        q.append(now-1)
        check[now-1] = True
        dist[now-1] = dist[now] + 1
        visit[now-1] = now
    if now +1 < MAX and not check[now+1]:
        q.append(now+1)
        check[now+1] = True
        dist[now+1] = dist[now] + 1
        visit[now+1] = now
    if now * 2< MAX and not check[now*2]:
        q.append(now*2)
        check[now*2] = True
        dist[now*2] = dist[now] + 1
        visit[now*2] = now

print(dist[M])
# print(visit)
def go(n, m):
    if n != m:
        go(n, visit[m])
    print(m, end=' ')
go(N, M)