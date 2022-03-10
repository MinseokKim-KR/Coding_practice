from collections import deque
import copy

M, N = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(M)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

ans = 0
def bfs():
    q = deque()
    temp_Map = copy.deepcopy(Map)
    for i in range(M):
        for j in range(N):
            if temp_Map[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<= nx < M and 0<= ny < N:
                if temp_Map[nx][ny] == 0:
                    temp_Map[nx][ny] = 2
                    q.append((nx, ny))
    temp_cnt=0
    for m in temp_Map:
        temp_cnt += m.count(0)
    global ans
    ans = max(ans, temp_cnt)

def Make_wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(M):
        for j in range(N):
            if Map[i][j] == 0:
                Map[i][j] = 1
                Make_wall(cnt+1)
                Map[i][j] = 0

Make_wall(0)
print(ans)