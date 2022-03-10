from itertools import combinations
N = int(input())
Arr = [list(map(int, input().split())) for _ in range(N)]
C = list(combinations([i for i in range(N)], N//2))
# print("C : ", C)
Result = 1000000000000000000000000000000000000
def Cal_Score(Map, Member):
    s = 0
    for mem in Member:
        s = s+Map[mem[0]][mem[1]] + Map[mem[1]][mem[0]]
    return s


for people in C:
    link = list(combinations(people, 2))
    temp_Member = [i for i in range(N)]
    for p in people:
        if p in temp_Member:
            del temp_Member[temp_Member.index(p)]
    star = list(combinations(temp_Member,2))
    S_link = Cal_Score(Arr, link)
    S_star = Cal_Score(Arr, star)
    if abs(S_link - S_star) < Result:
        Result = abs(S_link - S_star)
print(Result)