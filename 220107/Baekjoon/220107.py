# N, *Height = list(map(int, input().split()))
# print(Height)
# stack = []
# max_size = 0
# for idx, height in enumerate(Height):
#     min_point = idx
#     while stack and stack[-1][0] >= Height[idx]:
#         h, min_point = stack.pop()
#         tmp_size = h * (idx-min_point)
#         max_size = max(max_size, tmp_size)
#     stack.append([height, min_point])
#     # print("max_size : ", max_size)
#     # print("stack : ", stack)
# for h, point in stack:
#     max_size = max(max_size, (N-point) * h)
# print(max_size)

""""""
INF = int(1e9)
from collections import deque
W, H = map(int, input().split())
Map = [list(map(str, input())) for _ in range(H)]
def BFS(x,y):
    visited = [[INF] * W for _ in range(H)]
    q = deque()
    q.append([x, y])
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    while q:
        nx = x +