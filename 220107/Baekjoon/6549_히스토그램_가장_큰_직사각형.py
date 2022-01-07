N, *Height = list(map(int, input().split()))
# print(Height)
stack = []
max_size = 0
for idx, height in enumerate(Height):
    min_point = idx
    while stack and stack[-1][0] >= Height[idx]:
        h, min_point = stack.pop()
        tmp_size = h * (idx-min_point)
        max_size = max(max_size, tmp_size)
    stack.append([height, min_point])
    # print("max_size : ", max_size)
    # print("stack : ", stack)
for h, point in stack:
    max_size = max(max_size, (N-point) * h)
print(max_size)