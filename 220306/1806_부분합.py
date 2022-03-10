N, S = map(int, input().split())
A = list(map(int, input().split()))

# ans = N
# left = right = 0
# Sum = A[0]
# while left < right and right < N:
#     if Sum <=S:
#         right +=1
#         if right < N:
#             Sum += A[right]
#     elif Sum > S:
#         if ans > right-left+1:
#             ans = right - left + 1
#         Sum -= A[left]
#         left +=1

# print(ans)

from itertools import combinations
# ans = N
# A.sort()
# for i in range(1, N):
#     for C in list(combinations(A, i)):
#         if sum(C) > S:
#             ans = i
#             break
#     if ans != N:
#         break
left = right = 0
Sum = A[0]
# if S in A:
#     print(0)
# else:
#     while left <= right and right < N:
#         if Sum <S:
#             right +=1
#             if right < N:
#                 Sum += A[right]
#         elif Sum == S:
#             ans = min(right-left+1, ans)
#             right += 1
#             if right < N:
#                 Sum += A[right]
#         elif Sum > S:
#             ans = min(right-left+1, ans)
#             Sum -= A[left]
#             left +=1
#             if left > right and left < N:
#                 right = left
#                 Sum = A[left]
#     print(ans)

ans = N+1
while left <= right and right < N:
    if Sum <S:
        right +=1
        if right < N:
            Sum += A[right]
    elif Sum == S:
        ans = min(right-left+1, ans)
        right += 1
        if right < N:
            Sum += A[right]
    elif Sum > S:
        ans = min(right-left+1, ans)
        Sum -= A[left]
        left +=1
        if left > right and left < N:
            right = left
            Sum = A[left]
if ans > N:
    ans = 0
print(ans)