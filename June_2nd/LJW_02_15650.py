from itertools import combinations


N, M = map(int, input().split())

arr = [i + 1 for i in range(N)]

# 조합 
a = combinations(arr, M)

# 각 조합 출력
for i in a:
    print(*i)

# def dfs(start, combination):
#     if len(combination) == M:
#         print(*combination)
#         return
    
#     for i in range(start, N + 1):
#         combination.append(i)
#         dfs(i + 1, combination)
#         combination.pop()

# N, M = map(int, input().split())

# # DFS 
# dfs(1, [])