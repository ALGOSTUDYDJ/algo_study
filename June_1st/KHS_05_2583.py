
# 문제 풀이 순서를 따로 작성해 보았읍니다.
# 요즘 그냥 여유롭게 변수 이름이랑 문제 풀이 순서를
# 천천히 생각해서 푸니까 푸는 맛이 있네요. 쉬운 문제라 그럴까요?

import sys
sys.setrecursionlimit(10000)

dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
cnt = 1
# 4. 영역의 넓이를 구할 dfs 함수
def dfs(x, y):
    global cnt
    area[x][y] = 1
    for d in dir:
        ni = x + d[0]
        nj = y + d[1]
        if 0 <= ni < m and 0 <= nj < n and area[ni][nj] == 0:
            cnt += 1
            dfs(ni, nj)


m, n, k = map(int, input().split())

for_result = []

# 1. 영역 생성
area = [[0] * n for _ in range(m)]

# 2. 영역 칠하기
for _ in range(k):
    lx, ly, rx, ry = map(int, input().split())
    for i in range(ly, ry):
        for j in range(lx, rx):
            area[i][j] = 1

# 3. 영역을 순회하면서 칠하지 않은 부분이 있을 때 dfs 함수 실행
for i in range(m):
    for j in range(n):
        if area[i][j] == 0:
            dfs(i, j)
            for_result.append(cnt)
            # 함수로 영역의 넓이를 구했으면 영역의 넓이 초기화
            cnt = 1

# 5. 정렬해주고
for_result.sort()

# 6. 영역의 개수
print(len(for_result))

# 7. 각 영역의 넓이 출력
for result in for_result:
    print(result, end=" ")
