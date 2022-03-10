N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]

def up(Map):
    for j in range(N):
        pointer = 0
        for i in range(1, N):
            if Map[i][j]:
                if Map[pointer][j] == Map[i][j]:
                    Map[pointer][j] *= 2
                    Map[i][j] = 0
                elif Map[pointer][j] == 0:
                    Map[pointer][j] = Map[i][j]
                    Map[i][j] = 0
                    pointer += 1
                else:
                    pointer += 1
    return Map

# # UP
# def up(board):
#     for j in range(N):
#         pointer = 0
#         for i in range(1, N):
#             if board[i][j]:
#                 tmp = board[i][j]
#                 board[i][j] = 0
#                 # 포인터가 가리키는 수가 0일 때
#                 if board[pointer][j] == 0:
#                     board[pointer][j] = tmp
#                 # 포인터가 가리키는 수와 현재 위치의 수가 같을 때
#                 elif board[pointer][j]  == tmp:
#                     board[pointer][j] *= 2
#                     pointer += 1
#                 # 포인터가 가리키는 수와 현재 위치의 수가 다를 때
#                 else:
#                     pointer += 1
#                     board[pointer][j] = tmp
#     return board


print(up(Map))
                