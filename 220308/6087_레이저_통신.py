from collections import deque
W, H = map(int, input().split())
Map = [list(map(str, input())) for _ in range(H)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
C=[]
for i in range(H):
    for j in range(W):
        if Map[i][j] == 'C':
            C.append((i, j))
x1, y1, x2, y2 = C[0][0], C[0][1], C[1][0], C[1][1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited = [[-1] * W for _ in range(H)]
    visited[x][y] = 0
    while q:
        x, y= q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<= nx < H and 0<= ny < W:
                while 0<= nx < H and 0<= ny < W:
                    if Map[nx][ny] == '*':
                        break
                    if visited[nx][ny] == -1:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx, ny))
                    
                    nx += dx[i]
                    ny += dy[i]

    print(visited[x2][y2])

bfs(x1,y1)