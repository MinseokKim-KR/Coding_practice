from collections import deque
import copy

N, M = map(int, input().split())
Map = [list(map(int, input())) for _ in range(N)]


Wall = []
for i in range(N):
    for j in range(M):
        if Map[i][j] == 1:
            Wall.append((i, j))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 1000*1000
# def bfs(x, y):
#     temp_map = copy.deepcopy(Map)
#     temp_map[x][y] = 0
#     q = deque()
#     q.append((0,0))
#     while q:
#         x, y = q.popleft()
#         for i in range(4):
#             nx, ny = x+dx[i], y+dy[i]
#             if 0<= nx < N and 0<= ny < M:
#                 if temp_map[nx][ny] == 0:
#                     # temp_map[nx][ny] > temp_map[x][y]+1
#                     temp_map[nx][ny] = temp_map[x][y] + 1
#                     q.append((nx, ny))
#     return temp_map[N-1][M-1]

# for (x, y) in Wall:
#     # ans = min(ans, bfs(x,y))
#     cal = bfs(x, y)
#     if cal:
#         # print('cal : ', cal)
#         ans = min(ans, cal)
# if ans != 1000*1000:
#     print(ans+1)
# else:
#     print(-1)


def bfs():
    visited = [[[0]*2 for _ in range(M)] for __ in range(N)]
    visited[0][0][1] = 1
    q = deque()
    q.append((0,0,1))
    while q:
        x, y, w = q.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y][w]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<= nx < N and 0<= ny < M:
                if Map[nx][ny] == 1 and w ==1:
                    visited[nx][ny][0] = visited[x][y][1] + 1
                    q.append((nx, ny, 0))
                elif Map[nx][ny] == 0 and visited[nx][ny][w] == 0:
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    q.append((nx,ny,w))
    return -1

print(bfs())