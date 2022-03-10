N = int(input())
r1, c1, r2, c2 = map(int, input().split())
# print(r1, c1, r2, c2)

Map = [[-1] * (N+1) for _ in range(N+1)]
Map[r1][c1] = 0
from collections import deque

q = deque()
q.append((r1,c1))

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]
while q:
    r, c = q.popleft()
    for i in range(len(dx)):
        nr, nc = r + dx[i], c + dy[i]
        if 0<= nr <=N and 0<= nc <=N:
            if Map[nr][nc] == -1 or Map[nr][nc] > Map[r][c]+1:
                Map[nr][nc] = Map[r][c] + 1
                q.append((nr,nc))
print(Map[r2][c2])
