import math
N = int(input())
prime = []

#check prime
def is_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i ==0:
            return False
    return True

#Add prime
for i in range(2, N+1):
    if is_prime(i):
        prime.append(i)

print('prime : ', prime)
left = right = 0
Sum = prime[0]
ans = 0
while left <= right and right < len(prime):
    if Sum < N:
        right += 1
        if right < len(prime):
            Sum += prime[right]
    elif Sum == N:
        ans += 1
        right +=1 
        if right < len(prime):
            Sum += prime[right]
    elif Sum > N:
        Sum -= prime[left]
        left +=1 
        if left > right and left < len(prime):
            right = left
            Sum = prime[left]
print(ans)

prime = []
array = [True for _ in range(N + 1)]

for i in range(2, int(math.sqrt(N)) + 1):
    if array[i]:
        j = 2

        while i * j <= N:
            array[i * j] = False
            j += 1

for num in range(2, N + 1):
    if array[num]:
        prime.append(num)


ans = 0
left = right = 0
while right <= len(prime):
    Sum = sum(prime[left:right])
    if Sum == N:
        ans +=1
        right +=1
    elif Sum < N:
        right +=1
    else:
        left +=1
print(ans)