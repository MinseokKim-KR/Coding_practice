from collections import deque

N, M = map(int, input().split())
Ladder = [list(map(int, input().split())) for _ in range(N)]
Snake = [list(map(int, input().split())) for _ in range(M)]

dist = [-1] * 101
after = list(range(101))
for l in Ladder:
    after[l[0]] = l[1]
for s in Snake:
    after[s[0]] = s[1]

dist[1] = 0
q = deque()
q.append(1)

while q:
    now = q.popleft()
    for i in range(1, 7):
        next = now+i
        if next <=100:
            next_pos = after[next]
            if dist[next_pos] == -1:
                dist[next_pos] = dist[now] + 1
                q.append(next_pos)
print(dist[100])
