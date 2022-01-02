import copy
N, B = map(int, input().split())
Matrix = [list(map(int, input().split())) for _ in range(N)]

# 세번째 코드 : 분할정복으로 시간초과 해결, B = 1일때(1제곱일때), 1000의 나머지 해주는 부분 추가
def productMatrix(A, B):
    return [[sum(a*b for a,b in zip(A_row, B_col))%1000 for B_col in zip(*B)] for A_row in A]

def matrix_pow(A, n):
    if n == 1:
        for i in range(N):
            for j in range(N):
                A[i][j] %= 1000
        return A
    if n % 2 == 0:
        temp = matrix_pow(A, n//2)
        return productMatrix(temp, temp)
    else:
        temp = matrix_pow(A, n-1)
        return productMatrix(temp, A)

Result = matrix_pow(Matrix, B)
for R in Result:
    print(*R)


"""
초기 코드 -> 시간초과 실패
Result = copy.deepcopy(Matrix)
Temp = copy.deepcopy(Matrix)
while B > 1:
    Result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N): #3중 for문까지 하다보니 시간걸림
                Result[i][j] += (Temp[i][k] * Matrix[k][j])
            Result[i][j] %= 1000
    Temp = copy.deepcopy(Result)
    for R in Temp:
        print(R)
    print('======================')
    B -= 1
for R in Result:
    print(*R)
"""

"""
두번째 코드 -> 시간초과 실패
함수로 간소화 하였지만, 분할정복 사용하지 않아서 실패. 
Result = copy.deepcopy(Matrix)
def productMatrix(A, B):
    return [[sum(a*b for a,b in zip(A_row, B_col))%1000 for B_col in zip(*B)] for A_row in A]

for i in range(1,B):
    Result = productMatrix(Result, Matrix)
for R in Result:
    print(*R)
"""

