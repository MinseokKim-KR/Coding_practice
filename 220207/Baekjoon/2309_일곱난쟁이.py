nan = []
for _ in range(9):
    nan.append(int(input()))
# print('nan : ', nan)
nan.sort()
total = sum(nan)
breakPoint=False
for i in range(len(nan)):
    for j in range(i+1, len(nan)):
        if total - nan[i] - nan[j] == 100:
            for k in range(len(nan)):
                if k == i or k == j:
                    continue
                print(nan[k])
            breakPoint = True
        if breakPoint:
            break
    if breakPoint:
        break