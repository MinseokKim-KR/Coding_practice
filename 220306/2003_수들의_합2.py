N, M = map(int, input().split())
A = list(map(int, input().split()))
ans = 0

# pointer = 0
# while pointer < N:
#     for now in range(pointer, N+1):
#         if sum(A[pointer:now]) == M:
#             ans +=1
#         if sum(A[pointer:now]) > M:
#             break
#     pointer +=1
# print(ans)

Sum = A[0]
left = right = 0
while left <= right and right < N:
    if Sum < M:
        right +=1
        if right < N:
            Sum += A[right]
    elif Sum == M:
        ans +=1
        right +=1
        if right < N:
            Sum += A[right]
    elif Sum > M:
        Sum -= A[left]
        left +=1
        if left > right and left < N:
            right = left
            Sum = A[left]

print(ans)
