from collections import deque
N = int(input())
time = [[-1]*(N+1) for _ in range(N+1)]
q = deque()
q.append((1,0))
time[1][0] = 0
while q:
    s,c = q.popleft()
    if time[s][s] == -1:
        time[s][s] = time[s][c] + 1
        q.append((s,s))
    if s+c <= N and time[s+c][c] == -1:
        time[s+c][c] = time[s][c] + 1
        q.append((s+c, c))
    if s-1 >= 0 and time[s-1][c] == -1:
        time[s-1][c] = time[s][c] + 1
        q.append((s-1, c))

ans = -1
for i in range(N+1):
    if time[N][i] != -1:
        if ans == -1 or ans > time[N][i]:
            ans = time[N][i]

print(ans)