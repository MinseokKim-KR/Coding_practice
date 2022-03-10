from collections import deque

A, B, C = map(int, input().split())

ans = 0
Sum = A+B+C
visited = [[False] * 1501 for _ in range(1501)]

def bfs():
    q = deque()
    q.append((A,B))
    visited[A][B] = True
    while q:
        x, y = q.popleft()
        z = Sum-x-y
        if x == y == z:
            print(1)
            return
        for a, b in (x, y), (x, z), (y, z):
            if a < b:
                b -= a
                a += a
            elif a > b :
                a -= b 
                b += b 
            else:
                continue
            c = Sum-a-b
            X = min(a,b,c)
            Y = max(a,b,c)
            if not visited[X][Y]:
                q.append((X, Y))
                visited[X][Y] = True
    print(0)



if Sum % 3 != 0:
    print(0)
else:
    bfs()