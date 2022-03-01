N, M = map(int, input().split())
Friends = [[0]* N for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    Friends[a][b] = 1
    Friends[b][a] = 1

# check = 1
# for f in Friends:
#     print(f)
# for i in range(N-1):
#     # if i == N-1 :
#     #     if Friends[-1][i] != Friends[i][-1]:
#     #         check = 0
#     # else:
#     print('left : ', Friends[i][i+1])
#     print('right : ', Friends[i+1][i])
#     if Friends[i][i+1] != 1 or Friends[i+1][i] != 1:
#         check = 0 
# print(check)
