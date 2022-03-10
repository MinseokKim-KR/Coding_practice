N, M = map(int, input().split())
Map = [list(map(str, input())) for _ in range(N)]
# print(Map)

from collections import deque
import sys
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
rx, ry, bx, by = 0,0,0,0
visited = [[[[-1] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

for x, m in enumerate(Map):
    for y in range(len(m)):
        if Map[x][y] == 'R':
            rx = x
            ry = y
        if Map[x][y] == 'B':
            bx = x
            by = y

def move(x, y, dx, dy):
    cnt = 0
    while Map[x+dx][y+dy] != "#":
        if Map[x+dx][y+dy] == "O":
            return 0, 0, 0
        x += dx
        y += dy
        cnt +=1
    return x, y, cnt

def bfs(rx, ry, bx, by):
    global visited
    visited[rx][ry][bx][by] = 0
    q = deque()
    q.append((rx, ry, bx, by))
    while q:
        rx, ry, bx, by = q.popleft()
        for i in range(4):
            nrx, nry, rmove = move(rx, ry, dx[i], dy[i])
            nbx, nby, bmove = move(bx, by, dx[i], dy[i])
            if not nbx and not nby:
                continue
            elif nrx==0 and nry==0:
                print(visited[rx][ry][bx][by]+1)
                return
            elif nrx == nbx and nry == nby:
                if rmove > bmove:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            if visited[nrx][nry][nbx][nby] == -1:
                visited[nrx][nry][nbx][nby] = visited[rx][ry][bx][by] + 1
                q.append((nrx, nry, nbx, nby))
        if not q or visited[rx][ry][bx][by]>=10:
            print(-1)
            return
bfs(rx, ry, bx, by)