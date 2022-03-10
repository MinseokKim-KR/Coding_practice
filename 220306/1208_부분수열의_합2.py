from itertools import combinations
N, S = map(int, input().split())
A = list(map(int, input().split()))

l_sum, r_sum = [],[]

left, right = A[:N//2], A[N//2:]
for i in range(len(left)+1):
    C = combinations(left, i)
    for c in C:
        l_sum.append(sum(c))
for i in range(len(right)+1):
    C = combinations(right, i)
    for c in C:
        r_sum.append(sum(c))
l_sum.sort()
r_sum.sort()
print('left : ', left)
print('right : ', right)
print('l_sum : ', l_sum)
print('r_sum : ', r_sum)
ans = 0

left_p, right_p = 0, len(r_sum)-1
while left_p < len(l_sum) and right_p >=0:
    Sum = l_sum[left_p] + r_sum[right_p]
    if Sum == S:
        same_count_left = 1
        same_count_right = 1
        same_left_idx = left_p
        same_right_idx = right_p

        left_p += 1
        right_p -= 1
        while left_p < len(l_sum) and l_sum[left_p] == l_sum[same_left_idx]:
            same_count_left +=1
            left_p += 1
        while right_p >=0 and r_sum[right_p] == r_sum[same_right_idx]:
            same_count_right +=1
            right_p -= 1
        ans += same_count_left * same_count_right
    elif Sum < S:
        left_p += 1
    else: # Sum > S
        right_p -=1
if S == 0:
    ans -= 1
print(ans)
        
# import sys
# from itertools import combinations
# input = sys.stdin.readline

# n, s = map(int, input().split())
# arr = list(map(int, input().split()))

# # meet in the middle
# arr_1 = arr[:n//2]
# arr_2 = arr[n//2:]

# subsum_arr_1 = []
# subsum_arr_2 = []

# for i in range(len(arr_1) + 1):
#     # arr_1에서 0 ~ len(arr_1) + 1개만큼 뽑아 만들 수 있는 부분집합의 합을 구한다.
#     comb_1 = combinations(arr_1, i)
#     for comb in comb_1:
#         subsum_arr_1.append(sum(comb))

# for i in range(len(arr_2) + 1):
#     # arr_2에서 0 ~ len(arr_2) + 1개만큼 뽑아 만들 수 있는 부분집합의 합을 구한다.
#     comb_2 = combinations(arr_2, i)
#     for comb in comb_2:
#         subsum_arr_2.append(sum(comb))

# subsum_arr_1.sort()
# subsum_arr_2.sort()
# print('left : ', arr_1)
# print('right : ', arr_2)
# print('l_sum : ', subsum_arr_1)
# print('r_sum : ', subsum_arr_2)
# left_pointer = 0
# right_pointer = len(subsum_arr_2) - 1
# ans = 0

# while left_pointer < len(subsum_arr_1) and right_pointer >= 0:
#     tmp = subsum_arr_1[left_pointer] + subsum_arr_2[right_pointer]

#     # 두 포인터가 가르키는 값의 합이 s와 같다면
#     if tmp == s:

#         # 부분집합의 합이 같은 경우를 예외처리
#         same_count_left = 1
#         same_count_right = 1

#         same_left_idx = left_pointer
#         same_right_idx = right_pointer

#         left_pointer += 1
#         right_pointer -= 1

#         while left_pointer < len(subsum_arr_1) and subsum_arr_1[left_pointer] == subsum_arr_1[same_left_idx]:
#             same_count_left += 1
#             left_pointer += 1
        
#         while right_pointer >= 0 and subsum_arr_2[right_pointer] == subsum_arr_2[same_right_idx]:
#             same_count_right += 1
#             right_pointer -= 1
        
#         ans += same_count_left * same_count_right
    
#     elif tmp < s:
#         left_pointer += 1
    
#     else:
#         right_pointer -= 1

# # 아무것도 뽑지 않는 경우는 고려하지 않으므로, s가 0이라면 해당 경우의 수 1개를 빼준다
# if s == 0:
#     ans -= 1
    
# print(ans)