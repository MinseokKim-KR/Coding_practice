
def Rotate_90(M):
    return [list(row) for row in zip(*M[::-1])]

def Rotate_270(M):
    M = Rotate_90(M)
    M = Rotate_90(M)
    M = Rotate_90(M)
    return M

def Top_bottom_switch(M):
    for i in range(len(M) // 2):
        temp = M[len(M)-1-i]
        M[len(M)-1-i] = M[i]
        M[i] = temp
    return M

def Left_right_switch(M):
    M = list(map(list, zip(*M)))
    M = Top_bottom_switch(M)
    M = list(map(list, zip(*M)))
    return M


def operation5(a):
    n = len(a)
    m = len(a[0])
    ans = [[0]*m for _ in range(n)]
    for i in range(n//2):
        for j in range(m//2):
            ans[i][j+m//2] = a[i][j]
            ans[i+n//2][j+m//2] = a[i][j+m//2]
            ans[i+n//2][j] = a[i+n//2][j+m//2]
            ans[i][j] = a[i+n//2][j]
    return ans

def operation6(a):
    n = len(a)
    m = len(a[0])
    ans = [[0]*m for _ in range(n)]
    for i in range(n//2):
        for j in range(m//2):
            ans[i+n//2][j] = a[i][j]
            ans[i][j] = a[i][j+m//2]
            ans[i][j+m//2] = a[i+n//2][j+m//2]
            ans[i+n//2][j+m//2] = a[i+n//2][j]
    return ans

n,m,r = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
func = [Top_bottom_switch, Left_right_switch, Rotate_90, Rotate_270, operation5, operation6]
for op in map(int, input().split()):
    a = func[op-1](a)
for row in a:
    print(*row, sep=' ')