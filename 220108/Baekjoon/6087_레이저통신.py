from collections import deque

def bfs(x, y):
    q = deque()
    q.append([x,y])
    visited[x][y] = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            while True:
                ## 범위 벗어나면
                if not (0 <= nx < H and 0 <= ny < W):
                    break
                ## 벽을 만나면
                if board[nx][ny] == "*":
                    break
                ## 지났었지만, 현재가 더 많은 거울 필요하면
                if visited[nx][ny] < visited[x][y] + 1:
                    break
                ## board 업데이트, q 추가
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
                nx, ny = nx + dx[i], ny + dy[i]
            # print(visited)

W, H= map(int, input().split())
board = [list(map(str, input())) for _ in range(H)]
C = []
for i in range(H):
    for j in range(W):
        if board[i][j] == "C":
            C.append([i, j])
[sx, sy], [ex, ey] = C
visited = [[float("inf")] * W for _ in range(H)]
bfs(sx, sy)
print(visited[ex][ey] -1 )