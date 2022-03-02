from itertools import combinations

while 1:
    arr = list(map(int, input().split()))
    # print('arr: ', arr)
    k = arr[0]
    if k == 0:
        # print('K is 0')
        break
    ans = list(combinations(arr[1:], 6))
    for a in ans:
        print(*a)
    print('')
