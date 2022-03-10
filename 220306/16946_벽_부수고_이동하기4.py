from collections import deque
from collections import defaultdict
import copy
N, M = map(int, input().split())
Map = [list(map(int, input())) for _ in range(N)]

dx =[-1, 1, 0, 0]
dy =[0, 0, -1, 1]

# def bfs(x, y):
#     q = deque()
#     q.append((x, y))
#     cnt = 1
#     visited = [[-1] * M for _ in range(N)]
#     visited[x][y] = 1
#     while q:
#         x, y = q.popleft()
#         for i in range(4):
#             nx, ny = x+dx[i], y+dy[i]
#             if 0<= nx < N and 0<= ny < M:
#                 if visited[nx][ny] == -1 and Map[nx][ny] == 0:
#                     visited[nx][ny] = 1
#                     q.append((nx, ny))
#                     cnt +=1
#     return cnt

# for i in range(N):
#     for j in range(M):
#         if Map[i][j] == 1:
#             ans = bfs(i, j)
#             Map[i][j] = ans%10

# for m in Map:
#     print(*m, sep='')

def bfs(x, y, num):
    global Temp_Map
    q = deque()
    q.append((x, y))
    cnt = 1
    Temp_Map[x][y] = num
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<= nx < N and 0<= ny < M:
                if Temp_Map[nx][ny] == 0:
                    Temp_Map[nx][ny] = num
                    q.append((nx, ny))
                    cnt += 1
    return cnt

num = 2
Arr = defaultdict()
Temp_Map = copy.deepcopy(Map)
for i in range(N):
    for j in range(M):
        if Map[i][j] == 0:
            count = bfs(i, j, num)
            Arr[num] = count
            num +=1
# print(Arr)
# print(Temp_Map)
for i in range(N):
    for j in range(M):
        if Map[i][j] == 1:
            count = 1
            for idx in range(4):
                nx, ny = i + dx[idx], j + dy[idx]
                if 0<= nx < N and 0<= ny < M and Temp_Map[nx][ny] != 1:
                    count += Arr[Temp_Map[nx][ny]]
            Map[i][j] = count

# print("Result : ", Map)
for m in Map:
    print(*m, sep='')
