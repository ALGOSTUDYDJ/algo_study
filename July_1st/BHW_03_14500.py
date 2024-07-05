# 14500. 테트로미노

# 1. 각 지점들(깊이 1)을 순회하며 깊이 4까지 순회하며 누적합이 최대인 경우를 구한다.
# 2. T자 모양의 경우 별도로 계산한다.
# 3. 누적합이 최대인 경우를 출력한다.

import sys

input = sys.stdin.readline
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N, M = map(int, input().split())    # 세로, 가로
board = [list(map(int, input().split())) for _ in range(N)] # N*M 판
visited = [[0 for _ in range(M)] for _ in range(N)]         # 방문 배열
max_total = 0           # 최댓값

# dfs 함수
def dfs(t, depth, total):
    global max_total
    # 종료조건
    if depth == 4:
        # 최댓값 갱신
        if total > max_total:
            max_total = total
        return
    # 미종료 시 수행할 작업
    depth += 1
    for d in dirs:
        dr = t[0] + d[0]
        dc = t[1] + d[1]
        # 유효범위 내이면서 미방문시
        if 0 <= dr < N and 0 <= dc < M and not visited[dr][dc]:
            visited[dr][dc] = 1
            dfs((dr, dc), depth, total + board[dr][dc]) # dfs 탐색 진행
            visited[dr][dc] = 0

# 볼록할 철 모양
def checkT(t):
    global max_total
    direcs = []
    # 4방향에 대해 조사
    for d in dirs:
        dr = t[0] + d[0]
        dc = t[1] + d[1]
        if 0 <= dr < N and 0 <= dc < M:
            direcs.append(board[dr][dc])
    # 유효범위가 3방향이 안 되면 4칸 불가
    if len(direcs) < 3:
        return
    # 3칸이면 더해서 최댓값인지 확인
    elif len(direcs) == 3:
        pass
    # 4방향 모두 가능하면 가장 작은값 제거
    else:
        direcs.sort()
        direcs.pop(0)
    total = sum(direcs) + board[t[0]][t[1]]
    # 최댓값 갱신
    if total > max_total:
        max_total = total

# 모든 지점에 대해 탐색 수행
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs((i, j), 1, board[i][j]) # 깊이 4
        checkT((i, j))              # T자 탐색
        visited[i][j] = 0

print(max_total)