from collections import Counter
T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

ans = 0
sum_A, sum_B = [], []

for i in range(n):
    Sum = 0
    for j in range(i, n):
        Sum += A[j]
        sum_A.append(Sum)

for i in range(m):
    Sum = 0
    for j in range(i, m):
        Sum += B[j]
        sum_B.append(Sum)

sum_A.sort()
sum_B.sort()

c = Counter(sum_B)

# print("sum_A : ", sum_A)
# print("sum_B : ", sum_B)
# print("Counter : ", c)

ans = 0
for num in sum_A:
    ans += c[T-num]
print(ans)


"""
import bisect 
T = int(input()) 
N = int(input()) 
Aarr = list(map(int,input().split())) 
M = int(input()) 
Barr = list(map(int,input().split())) 
Asum = [] 
Bsum = [] 
for i in range(N): #O(A*(A-1)/2) 
	s = Aarr[i] 
	Asum.append(s) 
	for j in range(i+1,N): 
		s+=Aarr[j] 
		Asum.append(s) 

for i in range(M): #O(B*(B-1)/2) 
	s = Barr[i] 
	Bsum.append(s) 
	for j in range(i+1,M): 
		s+=Barr[j] 
		Bsum.append(s) 

Asum.sort() 
Bsum.sort() 
answer = 0 

for i in range(len(Asum)): 
	l = bisect.bisect_left(Bsum,T-Asum[i]) 
	r = bisect.bisect_right(Bsum,T-Asum[i]) 
	answer+=r-l 
print(answer)

출처: https://imksh.com/78 [강승현입니다]
"""