N, M = map(int, input().split())
c = [False] * (N+1)
a = [0] * N
def BF(index, start, n, m):
    if index == m:
        Print=''
        for i in range(m):
            Print += str(a[i]) + ' '
        print(Print)
        return
    for i in range(start, n+1):
        c[i] = True
        a[index] = i
        BF(index+1, i, n, m)
        c[i] = False

BF(0,1,N,M)