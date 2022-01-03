N = int(input())

# 네번째 : 피보나치수를 K로 나눈 나머지는 항상 같은 주기를 가진다!! 이를 피사노 주기라고 한다. https://www.acmicpc.net/blog/view/28
mod = 1000000
p = int(mod/10*15)
fibo = [0,1]
for i in range(2,p):
    fibo.append((fibo[i-1] + fibo[i-2]) % mod)

print(fibo[N%p])


"""
# 첫번째 : lambda 사용해서 해결 -> 1000 입력시, 재귀함수 호출 횟수 제한으로 인해 에러 발생
fib = lambda n, a=0, b=1 : a if n <= 0 else fib(n-1, b, a+b)

print(fib(N))
"""

"""
## https://shoark7.github.io/programming/algorithm/%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EC%9D%84-%ED%95%B4%EA%B2%B0%ED%95%98%EB%8A%94-5%EA%B0%80%EC%A7%80-%EB%B0%A9%EB%B2%95.html
# 위 사이트에서 사용한 일반항 사용하여 해결 진행 -> 1000 입력시 값이 다르게 나옴
def fibo(n):
    sqrt_5 = 5 ** (1/2)
    ans = 1 / sqrt_5 * ( ((1 + sqrt_5) / 2) ** n  - ((1 - sqrt_5) / 2) ** n )
    return int(ans)
print(fibo(N)%1000000)
"""


"""
# 세번째 : 행렬을 이용하여 문제 해결 -> 시간초과 발생으로 해결 안됨.
def fibo(n):
    SIZE = 2
    ZERO = [[1, 0], [0, 1]] # 행렬의 항등원
    BASE = [[1, 1], [1, 0]] # 곱셈을 시작해 나갈 기본 행렬

    # 두 행렬의 곱을 구한다
    def square_matrix_mul(a, b, size=SIZE):
        new = [[0 for _ in range(size)] for _ in range(size)]

        for i in range(size):
            for j in range(size):
                for k in range(size):
                    new[i][j] += a[i][k] * b[k][j]
        return new

    # 기본 행렬을 n번 곱한 행렬을 만든다
    def get_nth(n):
        matrix = ZERO.copy()
        k = 0
        tmp = BASE.copy()

        while 2 ** k <= n:
            if n & (1 << k) != 0:
                matrix = square_matrix_mul(matrix, tmp)
            k += 1
            tmp = square_matrix_mul(tmp, tmp)

        return matrix

    return get_nth(n)[1][0]

print(fibo(N)%1000000)
"""