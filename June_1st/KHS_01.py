
# 기본적인 dfs 문제입니다.

# 입력 받기
n, m= map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]

dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

cnt = 0

# dfs 함수 만들기
def dfs(x, y):
    if 0 <= x < n and 0 <= y < m and arr[x][y] == 0:
        arr[x][y] = 1
        for d in dir:
            ni = x + d[0]
            nj = y + d[1]
            dfs(ni, nj)
    else:
        return

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            dfs(i, j)
            cnt += 1

print(cnt)
