from itertools import combinations
N, K = map(int, input().split())

Arr = [input() for _ in range(N)]
ans = 0
if K < 5:
    print(ans)
else:
    for i in range(len(Arr)):
        word = list(set(Arr[i]).difference('a', 'c', 'i', 't', 'n'))
        Arr[i]= word
    Arr.sort(key= lambda x: len(x))
    print('sorted Arr : ', Arr)
    # K -= 4
    # for idx, word in enumerate(Arr):
    #     if K- len(word)>=0:
    #         K -= len(word)
    #         for i in range(len(Arr)):

    #         ans +=1

    # candidiate : 필수 글자를 제외한 알파벳
    # need : 필수 알파벳
    candidiate = ['b','d','e','f','g','h','j','k','l','m','o','p','q','r','s','u','v','w','x','y','z']
    need = ['a','c','t','i','n']
    for C in list(combinations(candidiate, K - 5)):
        each = 0
        res = 0
        for c in C:



    print(ans)
