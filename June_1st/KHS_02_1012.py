
# 재귀의 최대 깊이 한도를 설정할 수 있는 코드입니다.
# 이거 에러뜨길래 그냥 눌러서 확인해보니까 백준에서 자세하게 설명해줍니다.
import sys
sys.setrecursionlimit(10000)


# dfs 함수입니다.
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def dfs(x, y):
    if 0 <= x < m and 0 <= y < n and arr[x][y] == 1:
        arr[x][y] = 0
        for d in dir:
            ni = x + d[0]
            nj = y + d[1]
            dfs(ni, nj)
    else:
        return


case = int(input())
for _ in range(case):
    # 입력받기
    m, n, k = map(int, input().split())
    arr = [[0] * n for _ in range(m)]

    # 배추 심기
    for _ in range(k):
        a, b = map(int, input().split())
        arr[a][b] = 1

    # 필요한 벌레 수
    bug_cnt = 0
    
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1:
                dfs(i, j)
                bug_cnt += 1
    
    print(bug_cnt)
