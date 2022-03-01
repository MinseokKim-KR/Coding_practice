# from collections import deque

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# N, M = map(int, input().split())
# Map = [list(map(int, input())) for _ in range(M)]
# print("MAP : ", Map)
# q = deque()
# q.append((0, 0))

# while q:
#     x, y = q.popleft()
#     for i in range(4):
#         nx, ny = x + dx[i], y + dy[i]
#         if 0<= nx < M and 0<= ny < N:
#             if Map[nx][ny] >= Map[x][y] + 1 or Map[nx][ny] == 1 or Map[nx][ny] == 0:
#                 Map[nx][ny] = Map[x][y] + 1
#                 q.append((nx, ny))


# print(Map[M-1][N-1]-1)



from collections import deque
dx, dy = [0,0,-1, 1], [-1, 1, 0, 0]
M, N = map(int, input().split())
Map = [list(map(int, input())) for _ in range(N)]
dist = [[-1] * M for _ in range(N)]
q = deque()
q.append((0, 0))
dist[0][0] = 0
while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0<= nx < N and 0<= ny < M:
            if dist[nx][ny] == -1:
                if Map[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y]
                    q.appendleft((nx, ny))
                else:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
print(dist[N-1][M-1])